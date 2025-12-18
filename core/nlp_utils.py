import re

def preprocess(text: str) -> str:
    """
    Clean and normalize user input text.
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def detect_intent(text: str) -> str:
    """
    Detect intent based on keywords.
    """
    intents = {
        "sales_drop": ["drop", "decrease", "decline", "fall"],
        "sales_growth": ["increase", "growth", "rise"],
        "best_performance": ["best", "highest", "top"],
        "average": ["average", "mean"],
        "profit_loss": ["profit", "loss", "pnl"],
        "risk": ["risk", "volatility", "unstable"],
        "return": ["return", "roi"],
        "forecast_confidence": ["confidence", "certain", "sure"],
        "forecast_scenario": ["worst", "best case", "scenario"]
    }

    for intent, keywords in intents.items():
        if any(word in text for word in keywords):
            return intent

    return "unknown"
