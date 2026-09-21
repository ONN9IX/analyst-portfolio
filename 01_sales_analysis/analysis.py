from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "data" / "sales_data.csv"
df = pd.read_csv(DATA)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

required = {"order_id","order_date","customer_id","product_name","category","quantity","revenue"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

df["order_date"] = pd.to_datetime(df["order_date"], errors="raise")
if df["order_date"].dt.year.min() < 2023:
    raise ValueError("Dataset contains pre-2023 rows. Use a 2023+ dataset.")

print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())

orders = df.groupby("order_id", as_index=False).agg(
    revenue=("revenue","sum"),
    customer_id=("customer_id","first"),
    order_date=("order_date","min"),
)
print("\nRevenue:", round(df["revenue"].sum(), 2))
print("Orders:", df["order_id"].nunique())
print("Customers:", df["customer_id"].nunique())
print("Units:", df["quantity"].sum())
print("AOV:", round(orders["revenue"].mean(), 2))

monthly = df.assign(month=df["order_date"].dt.to_period("M").astype(str)).groupby("month",as_index=False).agg(
    revenue=("revenue","sum"), orders=("order_id","nunique")
)
print("\nMonthly:\n", monthly)
print("\nTop categories:\n", df.groupby("category")["revenue"].sum().sort_values(ascending=False).head(10))
print("\nTop products:\n", df.groupby("product_name")["revenue"].sum().sort_values(ascending=False).head(10))
