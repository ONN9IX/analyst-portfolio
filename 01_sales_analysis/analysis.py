from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "data" / "global_ecommerce_sales.csv"
df = pd.read_csv(DATA)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

required = {
    "order_id","order_date","customer_name","customer_segment","country",
    "region","product_category","product_name","quantity","unit_price"
}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

df["order_date"] = pd.to_datetime(df["order_date"], errors="raise")
if df["order_date"].dt.year.min() < 2023:
    raise ValueError("Dataset contains pre-2023 rows.")

for col in ["quantity","unit_price"]:
    df[col] = pd.to_numeric(df[col], errors="raise")
    if (df[col] < 0).any():
        raise ValueError(f"{col} contains negative values")

if df["order_id"].duplicated().any():
    raise ValueError("Expected one row per order, but duplicate order_id values were found.")

df["revenue"] = df["quantity"] * df["unit_price"]

print("Period:", df["order_date"].min().date(), "—", df["order_date"].max().date())
print("Rows:", len(df))
print("Missing values:\n", df.isna().sum())
print("Revenue:", round(df["revenue"].sum(), 2))
print("Orders:", df["order_id"].nunique())
print("Customers:", df["customer_name"].nunique())
print("Units:", int(df["quantity"].sum()))
print("AOV:", round(df.groupby("order_id")["revenue"].sum().mean(), 2))

monthly = (
    df.assign(month=df["order_date"].dt.to_period("M").astype(str))
      .groupby("month", as_index=False)
      .agg(revenue=("revenue","sum"), orders=("order_id","nunique"))
)
print("\nMonthly:\n", monthly)
print("\nCategories:\n", df.groupby("product_category")["revenue"].sum().sort_values(ascending=False))
print("\nTop products:\n", df.groupby("product_name")["revenue"].sum().sort_values(ascending=False).head(10))
print("\nSegments:\n", df.groupby("customer_segment")["revenue"].sum().sort_values(ascending=False))
print("\nRegions:\n", df.groupby("region")["revenue"].sum().sort_values(ascending=False))
