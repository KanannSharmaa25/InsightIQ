import pandas as pd


def compare_metric(series: pd.Series):
    """
    Compare latest value with previous value.
    Returns current, previous, percent change, and direction.
    """
    series = series.dropna()

    if len(series) < 2:
        return None

    current = series.iloc[-1]
    previous = series.iloc[-2]

    if previous == 0:
        pct_change = None
    else:
        pct_change = ((current - previous) / previous) * 100

    direction = "up" if current > previous else "down"

    return {
        "current": current,
        "previous": previous,
        "pct_change": pct_change,
        "direction": direction
    }
