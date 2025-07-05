# app/profiler.py

import pandas as pd

def profile_csv(file_path):
    df = pd.read_csv(file_path)

    report = {
        \"shape\": df.shape,
        \"columns\": list(df.columns),
        \"missing_values\": df.isnull().sum().to_dict(),
        \"duplicate_rows\": int(df.duplicated().sum()),
        \"numerical_stats\": df.describe().to_dict()
    }

    # Basic outlier detection using z-score (for demo)
    outliers = {}
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        col_zscore = ((df[col] - df[col].mean())/df[col].std()).abs()
        outliers[col] = int((col_zscore > 3).sum())
    report[\"outliers\"] = outliers

    return report

if __name__ == \"__main__\":
    audit = profile_csv(\"example.csv\")
    print(\"Audit Report:\\n\", audit)
