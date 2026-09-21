from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import confint_proportions_2indep

DATA = Path(__file__).parent / "data" / "cookie_cats.csv"

df = pd.read_csv(DATA)

required = {"userid", "version", "sum_gamerounds", "retention_1", "retention_7"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")

print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicate userid:", df["userid"].duplicated().sum())
print("\nGroup sizes:\n", df["version"].value_counts())

summary = df.groupby("version").agg(
    users=("userid", "nunique"),
    avg_rounds=("sum_gamerounds", "mean"),
    median_rounds=("sum_gamerounds", "median"),
    retention_1=("retention_1", "mean"),
    retention_7=("retention_7", "mean"),
)
print("\nSummary:\n", summary)

def retention_test(metric: str):
    table = pd.crosstab(df["version"], df[metric]).reindex(["gate_30", "gate_40"])
    chi2, p_value, _, _ = chi2_contingency(table)

    control = df.loc[df.version == "gate_30", metric].astype(int)
    test = df.loc[df.version == "gate_40", metric].astype(int)
    diff = test.mean() - control.mean()

    low, high = confint_proportions_2indep(
        count1=int(test.sum()), nobs1=len(test),
        count2=int(control.sum()), nobs2=len(control),
        method="wald"
    )

    rng = np.random.default_rng(42)
    boots = np.empty(5000)
    c = control.to_numpy()
    t = test.to_numpy()
    for i in range(len(boots)):
        boots[i] = rng.choice(t, len(t), replace=True).mean() - rng.choice(c, len(c), replace=True).mean()
    boot_low, boot_high = np.quantile(boots, [0.025, 0.975])

    print(f"\n{metric}")
    print(f"gate_30: {control.mean():.4%}")
    print(f"gate_40: {test.mean():.4%}")
    print(f"Difference (gate_40 - gate_30): {diff:.4%}")
    print(f"Chi-square p-value: {p_value:.6f}")
    print(f"95% analytical CI: [{low:.4%}, {high:.4%}]")
    print(f"95% bootstrap CI:  [{boot_low:.4%}, {boot_high:.4%}]")

for metric in ["retention_1", "retention_7"]:
    retention_test(metric)
