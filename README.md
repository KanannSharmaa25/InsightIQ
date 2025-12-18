# 📊 InsightIQ — Explainable Analytics & Forecasting Platform

InsightIQ is a **multi-mode data analytics platform** designed to help users **understand, analyze, and interpret data** using statistics, data science, and explainable AI techniques.

The project focuses on **clarity, transparency, and decision support**, rather than black-box predictions.

---

## 🚀 Key Features

### 🔁 Multi-Mode Analysis

* **Sales & Marketing Analytics**
* **Stock Market & Portfolio Analysis**
* **Prediction & Forecasting Mode**

Each mode adapts the analysis, metrics, and insights to the type of data provided.

---

### 🧪 Data Quality Dashboard

* Row and column counts
* Missing value detection
* Duplicate row detection
* Automatic date column identification

> Ensures users understand the reliability of their data before analysis.

---

### 🧭 Column Auto-Mapping

* Automatically detects:

  * Date columns
  * Target / value columns
* User can confirm or override mappings

> Makes the platform robust to messy, real-world CSV files.

---

### 📐 Statistical Analysis

* Mean, median, standard deviation
* Min / max values
* Confidence intervals (95%)

All statistics are **deterministic and explainable**.

---

### 📉 Metric Comparisons

* Latest vs previous period comparison
* Percentage change
* Direction indicators (↑ / ↓)

> Designed for executive-style decision making.

---

### 📈 Trend Strength Scoring

* Quantifies how strong a trend is (0–100)
* Labels trends as **Weak / Moderate / Strong**
* Indicates trend direction (upward / downward)

> Helps avoid over-interpreting noisy data.

---

### 🚩 Smart Alerts

Automatically flags:

* Significant sales drops
* High portfolio volatility
* Loss-making portfolios
* Forecast uncertainty

---

### 🧠 Storytelling Mode

Generates a **clear narrative summary** that explains:

* What changed
* Direction of key metrics
* Risks and uncertainties

> Converts raw numbers into understandable insights.

---

### 🤖 Ask AI (NLP-Based)

* Understands user questions using intent detection
* Answers are **strictly grounded in computed data**
* Avoids hallucinations and unsupported claims

---

### 🔮 Forecasting & Scenarios

* Time-series forecasting using historical trends
* Scenario-aware predictions:

  * Optimistic
  * Normal
  * Pessimistic
* Explicit uncertainty warnings

---

### 📤 Export & Usability

* Download processed data as CSV
* Download statistics summary
* Manual data entry supported
* Session reset controls

---

## 🧠 Design Philosophy

* **Explainability over black-box AI**
* **Deterministic logic before generative AI**
* **Clear uncertainty communication**
* **Real-world data robustness**

This project intentionally avoids claiming “accurate market prediction” and instead focuses on **decision support and analysis transparency**.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI & app framework)
* **Pandas & NumPy** (data processing)
* **Matplotlib** (visualization)
* **Scikit-learn concepts** (trend analysis)
* **Custom NLP logic** (intent detection)

---

## 📂 Project Structure

```
InsightIQ/
│
├── app.py
├── core/
│   ├── stats_engine.py
│   ├── data_quality.py
│   ├── column_mapper.py
│   ├── metrics_compare.py
│   ├── trend_strength.py
│   ├── storyteller.py
│   ├── insight_flags.py
│   ├── ai_explainer.py
│
├── modes/
│   ├── sales/
│   ├── stocks/
│   └── prediction/
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/InsightIQ.git
cd InsightIQ
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

## ⚠️ Disclaimer

This platform provides **data-driven insights and probabilistic forecasts** based on historical information.

* Predictions are **not guaranteed**
* No financial or investment advice is provided
* Results may change due to external factors

This project is intended for **educational and analytical purposes only**.

---

## 📌 Why This Project Stands Out

* Handles **real-world messy data**
* Prioritizes **explainability**
* Includes **storytelling & decision support**
* Avoids misleading AI claims
* Built like a **product**, not a demo

---

## 📸 Suggested Screenshots for GitHub

Include:

1. Mode selection screen
2. Data quality dashboard
3. Metric comparisons
4. Trend strength score
5. Storytelling summary
6. Forecasting with disclaimer

---

## 👤 Author

**Kanan Sharma**
Built as a portfolio-grade analytics project combining data science, statistics, and explainable AI principles.

---
