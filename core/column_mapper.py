def auto_map_columns(df):
    """
    Guess date and target columns based on column names and data types.
    """

    columns = df.columns.tolist()

    # Guess date column
    date_candidates = [
        col for col in columns
        if "date" in col.lower() or "time" in col.lower()
    ]
    guessed_date = date_candidates[0] if date_candidates else None

    # Guess numeric target column
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    priority_keywords = ["sales", "revenue", "price", "value", "amount", "profit"]

    guessed_target = None
    for key in priority_keywords:
        for col in numeric_cols:
            if key in col.lower():
                guessed_target = col
                break
        if guessed_target:
            break

    if guessed_target is None and numeric_cols:
        guessed_target = numeric_cols[0]

    return {
        "date_column": guessed_date,
        "target_column": guessed_target,
        "numeric_columns": numeric_cols
    }
