import numpy as np
import pandas as pd


def confidence_interval(series: pd.Series, confidence=0.95):
    mean = series.mean()
    std = series.std()
    n = series.count()

    margin = std * 1.96 / np.sqrt(n)  # 95% CI

    return {
        "mean": mean,
        "lower": mean - margin,
        "upper": mean + margin
    }
