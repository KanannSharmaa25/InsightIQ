def generate_flags(mode, df, insights=None):
    flags = []

    if mode == "sales" and "Sales" in df.columns:
        change = df["Sales"].pct_change()
        if (change < -0.2).any():
            flags.append("⚠️ Significant sales drop detected in one or more periods.")

    if mode == "stocks" and insights:
        if insights.get("volatility", 0) > 5:
            flags.append("⚠️ Portfolio volatility is high, indicating increased risk.")

        if insights.get("total_profit_loss", 0) < 0:
            flags.append("⚠️ Portfolio is currently at an overall loss.")

    if mode == "prediction":
        flags.append("ℹ️ Forecast uncertainty increases over longer horizons.")

    return flags
