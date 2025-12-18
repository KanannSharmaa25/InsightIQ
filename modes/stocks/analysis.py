import pandas as pd
import numpy as np


def stock_insights(df: pd.DataFrame):
    insights = {}

    if {"Buy_Price", "Current_Price", "Quantity"}.issubset(df.columns):
        df["Investment"] = df["Buy_Price"] * df["Quantity"]
        df["Current_Value"] = df["Current_Price"] * df["Quantity"]
        df["Profit_Loss"] = df["Current_Value"] - df["Investment"]
        df["Return_%"] = (df["Profit_Loss"] / df["Investment"]) * 100

        insights["total_investment"] = df["Investment"].sum()
        insights["current_value"] = df["Current_Value"].sum()
        insights["total_profit_loss"] = df["Profit_Loss"].sum()
        insights["average_return_percent"] = df["Return_%"].mean()
        insights["volatility"] = df["Return_%"].std()

    return insights
