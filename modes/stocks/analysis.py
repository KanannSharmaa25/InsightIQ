import pandas as pd


def stock_insights(df: pd.DataFrame, buy_col="Buy_Price", current_col="Current_Price", qty_col="Quantity"):
    """
    Compute stock/portfolio insights. Requires explicit column selection
    (buy price, current price, quantity) since these can't be reliably
    auto-detected the way a single date/target column can.
    """
    insights = {}

    required = {buy_col, current_col, qty_col}
    if not required.issubset(df.columns):
        return insights

    df = df.copy()
    df["Investment"] = df[buy_col] * df[qty_col]
    df["Current_Value"] = df[current_col] * df[qty_col]
    df["Profit_Loss"] = df["Current_Value"] - df["Investment"]
    df["Return_%"] = (df["Profit_Loss"] / df["Investment"]) * 100

    insights["total_investment"] = df["Investment"].sum()
    insights["current_value"] = df["Current_Value"].sum()
    insights["total_profit_loss"] = df["Profit_Loss"].sum()
    insights["average_return_percent"] = df["Return_%"].mean()
    insights["volatility"] = df["Return_%"].std()

    return insights