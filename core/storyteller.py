def generate_story(mode, comparisons, flags):
    """
    Generate a short narrative explaining what is happening in the data.
    """

    sentences = []

    # --- Trend direction ---
    ups = 0
    downs = 0

    for comp in comparisons.values():
        if comp["direction"] == "up":
            ups += 1
        elif comp["direction"] == "down":
            downs += 1

    if ups > downs:
        sentences.append(
            "Overall, key metrics show an upward trend compared to the previous period."
        )
    elif downs > ups:
        sentences.append(
            "Overall, several key metrics have declined compared to the previous period."
        )
    else:
        sentences.append(
            "Metrics show a mixed pattern with no strong overall direction."
        )

    # --- Mode-specific interpretation ---
    if mode == "sales":
        sentences.append(
            "This suggests changes in business performance that may be influenced by demand, pricing, or marketing activity."
        )

    elif mode == "stocks":
        sentences.append(
            "This reflects recent market movements affecting portfolio performance and risk exposure."
        )

    elif mode == "prediction":
        sentences.append(
            "These patterns inform future projections but remain subject to uncertainty."
        )

    # --- Risk & alerts ---
    if flags:
        sentences.append(
            "Some risk indicators or alerts were detected, which should be monitored closely."
        )
    else:
        sentences.append(
            "No major risk alerts were detected based on the current data."
        )

    # --- Disclaimer ---
    sentences.append(
        "These insights are derived from historical data and do not guarantee future outcomes."
    )

    return " ".join(sentences)
