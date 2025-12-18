import pandas as pd


def data_quality_report(df: pd.DataFrame):
    report = {}

    # Basic shape
    report["rows"] = df.shape[0]
    report["columns"] = df.shape[1]

    # Missing values
    missing = df.isnull().sum()
    report["missing_total"] = int(missing.sum())
    report["missing_columns"] = missing[missing > 0].to_dict()

    # Duplicate rows
    report["duplicate_rows"] = int(df.duplicated().sum())

    # Date column detection
    date_cols = [col for col in df.columns if "date" in col.lower()]
    report["date_columns"] = date_cols

    return report
