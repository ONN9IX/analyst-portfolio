from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).parent / "data" / "google_ads_jan_2024.csv"
df = pd.read_csv(DATA)
df.columns = df.columns.str.strip().str.lower()

required = {"company","campaign_type","conversion_rate","acquisition_cost","roi","clicks","impressions","date"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")

df["date"] = pd.to_datetime(df["date"], errors="raise")
if df["date"].dt.year.min() < 2023:
    raise ValueError("Dataset contains pre-2023 rows.")

numeric = ["conversion_rate","acquisition_cost","roi","clicks","impressions"]
for col in numeric:
    df[col] = pd.to_numeric(df[col], errors="raise")

if (df[["acquisition_cost","clicks","impressions"]] < 0).any().any():
    raise ValueError("Negative cost/click/impression values found.")

def div(a, b):
    return np.nan if b == 0 else a / b

cost = df["acquisition_cost"].sum()
clicks = df["clicks"].sum()
impressions = df["impressions"].sum()

print("Period:", df["date"].min().date(), "—", df["date"].max().date())
print("Rows:", len(df))
print("Impressions:", int(impressions))
print("Clicks:", int(clicks))
print("CTR:", f"{div(clicks, impressions):.2%}")
print("Acquisition Cost:", round(cost, 2))
print("CPC:", round(div(cost, clicks), 2))
print("Cost-weighted ROI:", round(np.average(df["roi"], weights=df["acquisition_cost"]), 2))
print("Click-weighted Conversion Rate:", f"{np.average(df['conversion_rate'], weights=df['clicks']):.2%}")

grouped = df.groupby("campaign_type").agg(
    cost=("acquisition_cost","sum"),
    clicks=("clicks","sum"),
    impressions=("impressions","sum"),
).reset_index()
grouped["ctr"] = grouped["clicks"] / grouped["impressions"]
grouped["cpc"] = grouped["cost"] / grouped["clicks"]
print("\nBy campaign type:\n", grouped.sort_values("ctr", ascending=False))
