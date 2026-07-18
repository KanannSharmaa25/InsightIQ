# InsightIQ

Multi-mode analytics and forecasting platform built with Streamlit.

---

## Key Features

### Multi-Mode Analysis

* **Sales & Marketing Analytics** — Analyze sales trends, growth/drop periods, and best/worst performance windows.
* **Stock Market & Portfolio Analysis** — Track investment, current value, profit/loss, and portfolio volatility.
* **Prediction & Forecasting Mode** — Linear trend forecasting with optimistic/pessimistic/normal scenario adjustments.

Each mode adapts the analysis, metrics, and insights to the type of data provided.

---

### Data Quality Dashboard

* Row and column counts
* Missing value detection
* Duplicate row detection
* Automatic date column identification

> Ensures users understand the reliability of their data before analysis.

---

### Column Auto-Mapping

* Automatically detects date columns and target/value columns
* User can confirm or override mappings via dropdowns

> Columns are detected by name patterns and data types, making the platform robust to differently-named CSV columns.

---

### Statistical Analysis

* Mean, median, standard deviation
* Min / max values
* Confidence intervals (95%) using z-score

All statistics are **deterministic and explainable**.

---

### Metric Comparisons

* Latest vs previous period comparison
* Percentage change
* Direction indicators (up / down)

---

### Trend Strength Scoring

* Quantifies how strong a trend is (0–100) using R-squared from linear regression (`numpy.polyfit`)
* Labels trends as **Weak / Moderate / Strong**
* Indicates trend direction (upward / downward)

> Helps avoid over-interpreting noisy data.

---

### Smart Alerts

Rule-based flags for:

* Significant sales drops (>20% period-over-period)
* High portfolio volatility (std > 5)
* Loss-making portfolios
* Long-horizon forecast warnings

---

### Storytelling Mode

Generates a **clear narrative summary** that explains:

* What changed (trend direction)
* Mode-specific context
* Whether risk alerts were detected

> Converts raw numbers into understandable insights.

---

### Ask AI

* Keyword-based intent detection — matches user questions against predefined keyword lists
* Answers are **grounded in computed data**
* Not a machine learning model; uses rule-based text matching

---

### Forecasting & Scenarios

* Time-series forecasting using linear regression extrapolation
* Scenario-aware predictions with fixed multipliers:

  * Optimistic (+10%)
  * Normal (baseline)
  * Pessimistic (-15%)
* Includes uncertainty warnings about forecast horizon

---

### Export & Usability

* Download processed data as CSV
* Manual data entry supported
* Session reset controls

---

## Design Philosophy

* **Explainability over black-box AI**
* **Deterministic logic before generative AI**
* **Clear uncertainty communication**
* **Real-world data robustness**

This project intentionally avoids claiming "accurate market prediction" and instead focuses on **decision support and analysis transparency**.

---

## Tech Stack

* **Python**
* **Streamlit** (UI & app framework)
* **Pandas & NumPy** (data processing, linear regression via `polyfit`)
* **Matplotlib** (visualization)

---

## Project Structure

```
InsightIQ/
├── app/
│   └── app.py              # Main Streamlit application
├── core/
│   ├── ai_explainer.py     # Keyword-based Q&A system
│   ├── column_mapper.py    # Automatic column detection
│   ├── confidence.py       # 95% confidence intervals
│   ├── data_quality.py     # Data quality reporting
│   ├── insight_flags.py    # Rule-based alert generation
│   ├── metrics_compare.py  # Period-over-period comparison
│   ├── nlp_utils.py        # Text preprocessing and intent detection
│   ├── stats_engine.py     # Basic descriptive statistics
│   ├── storyteller.py      # Narrative generation from data
│   ├── summary_generator.py# Mode-specific text summaries
│   ├── time_grouping.py    # Time-based aggregation
│   ├── trend_strength.py   # Trend scoring via linear regression
│   └── visuals.py          # Matplotlib trend plots
├── modes/
│   ├── prediction/
│   │   └── forecast.py     # Linear extrapolation with scenario multipliers
│   ├── sales/
│   │   └── analysis.py     # Sales-specific insights
│   └── stocks/
│       └── analysis.py     # Portfolio insights (P/L, volatility)
├── data/                   # Sample or uploaded data
├── requirements.txt
└── README.md
```

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/KanannSharmaa25/InsightIQ.git
cd InsightIQ
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app/app.py
```

---

## Disclaimer

This platform provides **data-driven insights and probabilistic forecasts** based on historical information.

* Predictions are **not guaranteed**
* No financial or investment advice is provided
* Results may change due to external factors

This project is intended for **educational and analytical purposes only**.

---

## Author

Kanan Sharma  
Portfolio project focused on applied data science, statistical analysis, and explainable AI.
