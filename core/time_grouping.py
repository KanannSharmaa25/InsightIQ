import pandas as pd


def group_by_time(df, date_col, freq):
    """
    Group dataframe by time frequency.
    freq: 'D' (daily), 'W' (weekly), 'M' (monthly), 'Y' (yearly)
    """
    df = df.copy()

    if date_col not in df.columns:
        return df

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col])

    grouped = (
        df.set_index(date_col)
          .groupby(pd.Grouper(freq=freq))
          .mean(numeric_only=True)
          .reset_index()
    )

    return grouped
