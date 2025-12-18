import pandas as pd


def basic_statistics(df: pd.DataFrame):
    """
    Returns basic statistical summary for numerical columns.
    """
    numeric_df = df.select_dtypes(include="number")

    stats = {
        "mean": numeric_df.mean(),
        "median": numeric_df.median(),
        "std_dev": numeric_df.std(),
        "min": numeric_df.min(),
        "max": numeric_df.max(),
    }

    return stats
