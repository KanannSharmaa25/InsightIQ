import pandas as pd
import numpy as np


def forecast_values(df, target_column, periods=12, scenario="normal"):
    """
    Forecast future values using a simple linear trend model.
    Returns forecast range based on scenario.
    """

    y = df[target_column].dropna().values
    x = np.arange(len(y))

    # Linear trend
    coef = np.polyfit(x, y, 1)
    trend = np.poly1d(coef)

    future_x = np.arange(len(y), len(y) + periods)
    base_forecast = trend(future_x)

    # Scenario adjustment
    if scenario == "optimistic":
        factor = 1.10
    elif scenario == "pessimistic":
        factor = 0.85
    else:
        factor = 1.0

    adjusted_forecast = base_forecast * factor

    return adjusted_forecast
