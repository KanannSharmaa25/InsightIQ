import numpy as np
import pandas as pd


def trend_strength(series: pd.Series):
    """
    Calculate trend strength score (0–100) using linear fit.
    Returns score, direction, and label.
    """
    series = series.dropna()

    if len(series) < 3:
        return None

    y = series.values
    x = np.arange(len(y))

    # Linear fit
    slope, intercept = np.polyfit(x, y, 1)
    y_pred = slope * x + intercept

    # R-squared
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)

    if ss_tot == 0:
        r2 = 0
    else:
        r2 = 1 - (ss_res / ss_tot)

    score = int(max(0, min(100, r2 * 100)))

    direction = "upward" if slope > 0 else "downward"

    if score < 40:
        label = "Weak"
    elif score < 70:
        label = "Moderate"
    else:
        label = "Strong"

    return {
        "score": score,
        "direction": direction,
        "label": label
    }
