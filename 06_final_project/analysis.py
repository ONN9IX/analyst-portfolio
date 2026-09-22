from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "data" / "global_ecommerce_sales.csv"
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df.columns = df.columns.str.strip().str.lower()
df["order_date"] = pd.to_datetime(df["order_date"], errors="raise")

required = {"order_id","order_date","customer_name","customer_segment","country","region",
            "product_category","product_name","quantity","total_sales","shipping_cost","profit"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")
if df["order_date"].dt.year.min() < 2023:
    raise ValueError("Pre-2023 rows found.")
if df["order_id"].duplicated().any():
    raise ValueError("Duplicate order_id found.")

for col in ["quantity","total_sales","shipping_cost","profit"]:
    df[col] = pd.to_numeric(df[col], errors="raise")

kpi = pd.DataFrame([{
    "period_start": df["order_date"].min().date(),
    "period_end": df["order_date"].max().date(),
    "orders": df["order_id"].nunique(),
    "customers": df["customer_name"].nunique(),
    "units": int(df["quantity"].sum()),
    "revenue": round(df["total_sales"].sum(), 2),
    "profit": round(df["profit"].sum(), 2),
    "aov": round(df["total_sales"].sum()/df["order_id"].nunique(), 2),
    "profit_margin": round(df["profit"].sum()/df["total_sales"].sum(), 4),
    "shipping_cost": round(df["shipping_cost"].sum(), 2),
}])
kpi.to_csv(OUT / "kpi_summary.csv", index=False)

monthly = (df.assign(month=df["order_date"].dt.to_period("M").astype(str))
             .groupby("month", as_index=False)
             .agg(revenue=("total_sales","sum"), profit=("profit","sum"), orders=("order_id","nunique")))
monthly["mom_revenue_pct"] = monthly["revenue"].pct_change() * 100
monthly.to_csv(OUT / "monthly_performance.csv", index=False)

category = df.groupby("product_category", as_index=False).agg(
    revenue=("total_sales","sum"), profit=("profit","sum"), units=("quantity","sum"), orders=("order_id","nunique"))
category["profit_margin"] = category["profit"] / category["revenue"]
category.sort_values("revenue", ascending=False).to_csv(OUT / "category_performance.csv", index=False)

region = df.groupby("region", as_index=False).agg(
    revenue=("total_sales","sum"), profit=("profit","sum"), orders=("order_id","nunique"))
region.to_csv(OUT / "region_performance.csv", index=False)

customer = df.groupby("customer_name", as_index=False).agg(
    orders=("order_id","nunique"), revenue=("total_sales","sum"), profit=("profit","sum"))
customer["repeat_customer"] = customer["orders"] > 1
customer.sort_values("revenue", ascending=False).to_csv(OUT / "customer_performance.csv", index=False)

print(kpi.to_string(index=False))
print("Repeat customer rate:", f"{customer['repeat_customer'].mean():.2%}")
