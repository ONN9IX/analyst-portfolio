from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).parent / "data" / "marketing_data.csv"
df = pd.read_csv(DATA)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

required = {"date","channel","spend","impressions","clicks","customers_acquired","revenue"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

df["date"] = pd.to_datetime(df["date"], errors="raise")
if df["date"].dt.year.min() < 2023:
    raise ValueError("Dataset contains pre-2023 rows. Use a 2023+ dataset.")

for col in ["spend","impressions","clicks","customers_acquired","revenue"]:
    df[col] = pd.to_numeric(df[col], errors="raise")
    if (df[col] < 0).any():
        raise ValueError(f"{col} contains negative values")

print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())

channel = df.groupby("channel", as_index=False).agg(
    spend=("spend","sum"),
    impressions=("impressions","sum"),
    clicks=("clicks","sum"),
    customers=("customers_acquired","sum"),
    revenue=("revenue","sum"),
)

def safe_divide(a, b):
    return np.divide(a, b, out=np.full(len(a), np.nan, dtype=float), where=b.to_numpy() != 0)

channel["ctr"] = safe_divide(channel["clicks"], channel["impressions"])
channel["cpc"] = safe_divide(channel["spend"], channel["clicks"])
channel["conversion_rate"] = safe_divide(channel["customers"], channel["clicks"])
channel["cac"] = safe_divide(channel["spend"], channel["customers"])
channel["roas"] = safe_divide(channel["revenue"], channel["spend"])
channel["roi"] = safe_divide(channel["revenue"] - channel["spend"], channel["spend"])

print("\nChannel performance:\n", channel.sort_values("roi", ascending=False, na_position="last"))
