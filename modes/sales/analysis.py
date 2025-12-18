import pandas as pd


def sales_insights(df: pd.DataFrame):
    insights = {}

    if "Sales" in df.columns:
        df["Sales_Change"] = df["Sales"].diff()

        insights["total_sales"] = df["Sales"].sum()
        insights["average_sales"] = df["Sales"].mean()
        insights["max_sales"] = df["Sales"].max()
        insights["min_sales"] = df["Sales"].min()

        insights["best_period"] = df.loc[df["Sales"].idxmax(), "Date"]
        insights["worst_period"] = df.loc[df["Sales"].idxmin(), "Date"]

        insights["growth_periods"] = int((df["Sales_Change"] > 0).sum())
        insights["drop_periods"] = int((df["Sales_Change"] < 0).sum())

    return insights
