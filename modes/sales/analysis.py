import pandas as pd


def sales_insights(df: pd.DataFrame, date_col: str = None, target_col: str = "Sales"):
    """
    Compute sales insights using the mapped date/target columns
    instead of assuming fixed column names.
    """
    insights = {}

    if target_col not in df.columns:
        return insights

    df = df.copy()
    df["_change"] = df[target_col].diff()

    insights["total_sales"] = df[target_col].sum()
    insights["average_sales"] = df[target_col].mean()
    insights["max_sales"] = df[target_col].max()
    insights["min_sales"] = df[target_col].min()

    if date_col and date_col in df.columns:
        insights["best_period"] = df.loc[df[target_col].idxmax(), date_col]
        insights["worst_period"] = df.loc[df[target_col].idxmin(), date_col]

    insights["growth_periods"] = int((df["_change"] > 0).sum())
    insights["drop_periods"] = int((df["_change"] < 0).sum())

    return insights