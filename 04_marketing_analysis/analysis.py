from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "data" / "marketing_data.csv"
df = pd.read_csv(DATA)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicates:", df.duplicated().sum())

required = {"date", "channel", "spend", "impressions", "clicks", "customers_acquired", "revenue"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

df["date"] = pd.to_datetime(df["date"])
df = df[df["date"].dt.year >= 2023].copy()

channel = df.groupby("channel", as_index=False).agg(
    spend=("spend", "sum"),
    impressions=("impressions", "sum"),
    clicks=("clicks", "sum"),
    customers=("customers_acquired", "sum"),
    revenue=("revenue", "sum"),
)
channel["ctr"] = channel["clicks"] / channel["impressions"]
channel["cpc"] = channel["spend"] / channel["clicks"]
channel["conversion_rate"] = channel["customers"] / channel["clicks"]
channel["cac"] = channel["spend"] / channel["customers"]
channel["roas"] = channel["revenue"] / channel["spend"]
channel["roi"] = (channel["revenue"] - channel["spend"]) / channel["spend"]

print("\nChannel performance:\n", channel.sort_values("roi", ascending=False))
