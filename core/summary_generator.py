def generate_summary(mode, df, stats, insights=None):
    """
    Generate a concise, professional summary based on mode and computed results.
    """

    # ---------- SALES MODE ----------
    if mode == "sales" and "Sales" in df.columns:
        avg_sales = stats["mean"].get("Sales", 0)
        max_sales = df["Sales"].max()
        min_sales = df["Sales"].min()

        return (
            f"Sales analysis indicates an average sales value of {avg_sales:.2f}. "
            f"The strongest sales performance reached {max_sales:.0f}, while the lowest observed "
            f"value was {min_sales:.0f}. Overall trends suggest relatively stable demand, "
            "with fluctuations across periods. These insights are based on historical data only."
        )

    # ---------- STOCK MODE ----------
    if mode == "stocks" and insights:
        total_pl = insights.get("total_profit_loss", 0)
        volatility = insights.get("volatility", 0)

        pl_text = "profit" if total_pl >= 0 else "loss"

        return (
            f"The portfolio currently reflects an overall {pl_text} of {abs(total_pl):.2f}. "
            f"Observed volatility is {volatility:.2f}, indicating a moderate level of risk. "
            "Portfolio performance is based on historical pricing and does not guarantee future returns."
        )

    # ---------- PREDICTION MODE ----------
    if mode == "prediction":
        return (
            "Forecast results indicate potential future trends based on historical patterns "
            "and selected scenarios. Predictions are probabilistic and subject to uncertainty. "
            "External factors may significantly impact actual outcomes."
        )

    return "Insufficient data available to generate an automated summary."
