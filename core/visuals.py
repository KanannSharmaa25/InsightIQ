import matplotlib.pyplot as plt
import pandas as pd


def plot_trends(df: pd.DataFrame):
    """
    Generate simple trend plots for numerical columns.
    """
    numeric_cols = df.select_dtypes(include="number").columns
    figures = []

    for col in numeric_cols:
        fig, ax = plt.subplots()
        ax.plot(df.index, df[col])
        ax.set_title(f"{col} Trend")
        ax.set_xlabel("Index")
        ax.set_ylabel(col)
        ax.grid(True)

        figures.append(fig)

    return figures
