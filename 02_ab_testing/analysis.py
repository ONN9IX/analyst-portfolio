from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import confint_proportions_2indep

BASE = Path(__file__).parent
DATA = BASE / "data" / "cookie_cats.csv"
OUT = BASE / "results"
OUT.mkdir(exist_ok=True)

if not DATA.exists():
    raise FileNotFoundError(
        "data/cookie_cats.csv not found. Run: python download_data.py"
    )

df = pd.read_csv(DATA)
required = {"userid", "version", "sum_gamerounds", "retention_1", "retention_7"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")
if df[list(required)].isna().any().any():
    raise ValueError("Missing values found in required columns.")
if df["userid"].duplicated().any():
    raise ValueError("Duplicate userid values found.")
if set(df["version"]) != {"gate_30", "gate_40"}:
    raise ValueError(f"Unexpected experiment groups: {sorted(df['version'].unique())}")

for metric in ["retention_1", "retention_7"]:
    if not pd.api.types.is_bool_dtype(df[metric]):
        normalized = df[metric].astype(str).str.lower().map({"true": True, "false": False})
        if normalized.isna().any():
            raise ValueError(f"{metric} must contain only True/False values.")
        df[metric] = normalized

df["sum_gamerounds"] = pd.to_numeric(df["sum_gamerounds"], errors="raise")
if (df["sum_gamerounds"] < 0).any():
    raise ValueError("Negative sum_gamerounds found.")

summary = df.groupby("version").agg(
    users=("userid", "nunique"),
    avg_rounds=("sum_gamerounds", "mean"),
    median_rounds=("sum_gamerounds", "median"),
    retention_1=("retention_1", "mean"),
    retention_7=("retention_7", "mean"),
)
print("Shape:", df.shape)
print("\nSummary:\n", summary)

rows = []
rng = np.random.default_rng(42)

for metric in ["retention_1", "retention_7"]:
    control = df.loc[df["version"] == "gate_30", metric].astype(int).to_numpy()
    test = df.loc[df["version"] == "gate_40", metric].astype(int).to_numpy()

    table = np.array([
        [len(control) - control.sum(), control.sum()],
        [len(test) - test.sum(), test.sum()],
    ])
    _, p_value, _, _ = chi2_contingency(table, correction=True)

    control_rate = control.mean()
    test_rate = test.mean()
    diff = test_rate - control_rate

    ci_low, ci_high = confint_proportions_2indep(
        count1=int(test.sum()), nobs1=len(test),
        count2=int(control.sum()), nobs2=len(control),
        method="wald", compare="diff",
    )

    boots = np.empty(5000)
    for i in range(boots.size):
        boots[i] = (
            rng.choice(test, len(test), replace=True).mean()
            - rng.choice(control, len(control), replace=True).mean()
        )
    boot_low, boot_high = np.quantile(boots, [0.025, 0.975])

    rows.append({
        "metric": metric,
        "gate_30_users": len(control),
        "gate_40_users": len(test),
        "gate_30_retained": int(control.sum()),
        "gate_40_retained": int(test.sum()),
        "gate_30_rate": control_rate,
        "gate_40_rate": test_rate,
        "difference_gate40_minus_gate30": diff,
        "chi_square_p_value": p_value,
        "ci_95_low": ci_low,
        "ci_95_high": ci_high,
        "bootstrap_ci_95_low": boot_low,
        "bootstrap_ci_95_high": boot_high,
    })

results = pd.DataFrame(rows)
results.to_csv(OUT / "retention_results.csv", index=False)

print("\nRetention tests:")
print(results.to_string(index=False))
print("\nMax game rounds:", int(df["sum_gamerounds"].max()))
