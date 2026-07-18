import streamlit as st
import pandas as pd

from core.stats_engine import basic_statistics
from core.visuals import plot_trends
from core.confidence import confidence_interval
from core.insight_flags import generate_flags
from core.summary_generator import generate_summary
from core.ai_explainer import answer_question
from core.storyteller import generate_story

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="InsightIQ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## ⚙️ Controls")

    if st.button("🔄 Reset Session"):
        st.session_state.clear()
        st.rerun()

    st.markdown("---")
    st.markdown("**InsightIQ**")
    st.caption("Explainable analytics & forecasting platform")

# ---------------- GLOBAL STYLES ----------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
        .block-container { padding-top: 2rem; padding-bottom: 2rem; }
        .mode-card {
            padding: 1.5rem;
            border-radius: 12px;
            background-color: #f8f9fa;
            border: 1px solid #e5e7eb;
            margin-bottom: 1rem;
        }
        .disclaimer { font-size: 0.9rem; color: #6b7280; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- HEADER ----------------
st.title("InsightIQ")
st.subheader("Multi-Mode Analytics & Prediction Platform")

st.markdown(
    """
    <div class="disclaimer">
    ⚠️ <b>Disclaimer:</b><br>
    This platform provides data-driven analysis and probabilistic forecasts.
    Predictions are <b>not guaranteed</b>. For educational purposes only.
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ---------------- MODE SELECTION ----------------
st.markdown("### Select Analysis Mode")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='mode-card'><h4>📊 Sales</h4></div>", unsafe_allow_html=True)
    if st.button("Enter Sales Mode"):
        st.session_state["mode"] = "sales"

with col2:
    st.markdown("<div class='mode-card'><h4>📈 Stocks</h4></div>", unsafe_allow_html=True)
    if st.button("Enter Stock Mode"):
        st.session_state["mode"] = "stocks"

with col3:
    st.markdown("<div class='mode-card'><h4>🔮 Prediction</h4></div>", unsafe_allow_html=True)
    if st.button("Enter Prediction Mode"):
        st.session_state["mode"] = "prediction"

st.divider()

mode = st.session_state.get("mode")
if not mode:
    st.info("Please select a mode above.")
    st.stop()

st.success(f"Current Mode: **{mode.capitalize()}**")

# ---------------- DATA INPUT ----------------
st.divider()
st.markdown("### 📂 Provide Your Data")

input_method = st.radio(
    "How would you like to provide data?",
    ["Upload CSV", "Enter data manually"],
    horizontal=True,
)

df = None

if input_method == "Upload CSV":
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

elif input_method == "Enter data manually":
    if mode == "sales":
        cols = ["Date", "Sales"]
    elif mode == "stocks":
        cols = ["Date", "Buy_Price", "Current_Price", "Quantity"]
    else:
        cols = ["Date", "Value"]

    edited_df = st.data_editor(pd.DataFrame(columns=cols), num_rows="dynamic")
    if st.button("Use this data") and not edited_df.empty:
        df = edited_df

if df is None:
    st.stop()

st.dataframe(df, use_container_width=True)

# ---------------- DATA QUALITY DASHBOARD ----------------
st.divider()
st.markdown("### 🧪 Data Quality Check")

from core.data_quality import data_quality_report

dq = data_quality_report(df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", dq["rows"])
    st.metric("Columns", dq["columns"])

with col2:
    st.metric("Missing Values", dq["missing_total"])
    st.metric("Duplicate Rows", dq["duplicate_rows"])

with col3:
    if dq["date_columns"]:
        st.success(f"Date column detected: {', '.join(dq['date_columns'])}")
    else:
        st.warning("No date column detected")

if dq["missing_columns"]:
    st.warning("Missing values detected in columns:")
    st.json(dq["missing_columns"])

# ---------------- COLUMN AUTO-MAPPING ----------------
st.divider()
st.markdown("### 🧭 Column Mapping")

from core.column_mapper import auto_map_columns

mapping = auto_map_columns(df)

date_col = st.selectbox(
    "Select Date Column",
    options=[None] + df.columns.tolist(),
    index=(df.columns.tolist().index(mapping["date_column"]) + 1)
    if mapping["date_column"] in df.columns else 0,
    help="Choose the column representing dates or time"
)

target_col = st.selectbox(
    "Select Target / Value Column",
    options=mapping["numeric_columns"],
    index=mapping["numeric_columns"].index(mapping["target_column"])
    if mapping["target_column"] in mapping["numeric_columns"] else 0,
    help="This column will be used for trends, statistics, and forecasting"
)

# Store confirmed mapping
st.session_state["date_column"] = date_col
st.session_state["target_column"] = target_col

# ---------------- STOCK-SPECIFIC COLUMN MAPPING ----------------
buy_col = current_col = qty_col = None

if mode == "stocks":
    st.divider()
    st.markdown("### 💰 Portfolio Column Mapping")
    st.caption("Stock mode needs three specific fields — these can't be auto-guessed like a single target column.")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    stock_col1, stock_col2, stock_col3 = st.columns(3)
    with stock_col1:
        buy_col = st.selectbox("Buy Price column", options=numeric_cols,
                                index=numeric_cols.index("Buy_Price") if "Buy_Price" in numeric_cols else 0)
    with stock_col2:
        current_col = st.selectbox("Current Price column", options=numeric_cols,
                                    index=numeric_cols.index("Current_Price") if "Current_Price" in numeric_cols else 0)
    with stock_col3:
        qty_col = st.selectbox("Quantity column", options=numeric_cols,
                                index=numeric_cols.index("Quantity") if "Quantity" in numeric_cols else 0)

# ---------------- TIME GROUPING ----------------
st.divider()
st.markdown("### ⏱ Time Aggregation")

date_col = st.session_state.get("date_column")

if date_col:
    freq_label = st.selectbox(
        "Group data by",
        ["Daily", "Weekly", "Monthly", "Yearly"],
        help="Aggregate data over time for clearer trends"
    )

    freq_map = {
        "Daily": "D",
        "Weekly": "W",
        "Monthly": "M",
        "Yearly": "Y"
    }

    from core.time_grouping import group_by_time

    df = group_by_time(df, date_col, freq_map[freq_label])

    st.success(f"Data grouped by {freq_label.lower()}.")
else:
    st.info("Select a date column to enable time grouping.")

# ---------------- STATS ----------------
st.divider()
st.markdown("### 📊 Statistical Analysis")

stats = basic_statistics(df)
for k, v in stats.items():
    st.markdown(f"**{k.capitalize()}**")
    st.dataframe(v.to_frame(name=k))

# ---------------- METRIC COMPARISONS ----------------
st.divider()
st.markdown("### 📉 Metric Comparisons (Latest vs Previous)")

from core.metrics_compare import compare_metric

numeric_cols = df.select_dtypes(include="number").columns
comparisons = {}

if len(numeric_cols) == 0:
    st.info("No numeric columns available for comparison.")
else:
    for col in numeric_cols:
        comparison = compare_metric(df[col])

        if comparison is None:
            continue

        comparisons[col] = comparison

        arrow = "⬆️" if comparison["direction"] == "up" else "⬇️"

        delta_text = (
            f"{arrow} {comparison['pct_change']:.2f}%"
            if comparison["pct_change"] is not None
            else "N/A"
        )

        st.metric(
            label=col,
            value=f"{comparison['current']:.2f}",
            delta=delta_text,
            help="Comparison between latest and previous values"
        )

# ---------------- TREND STRENGTH ----------------
st.divider()
st.markdown("### 📈 Trend Strength")

from core.trend_strength import trend_strength

target_col = st.session_state.get("target_column")

if target_col and target_col in df.columns:
    trend = trend_strength(df[target_col])

    if trend:
        st.metric(
            "Trend Strength Score",
            f"{trend['score']} / 100",
            help="Higher score means a clearer and more consistent trend"
        )

        st.markdown(
            f"**Trend Direction:** {trend['direction'].capitalize()}  \n"
            f"**Trend Quality:** {trend['label']}"
        )
    else:
        st.info("Not enough data points to evaluate trend strength.")
else:
    st.info("Select a target column to evaluate trend strength.")

# ---------------- CONFIDENCE INTERVALS ----------------
st.divider()
st.markdown("### 📐 Confidence Intervals (95%)")
st.caption("Ranges where the true mean likely lies based on historical data.")

for col in df.select_dtypes(include="number").columns:
    ci = confidence_interval(df[col])
    st.markdown(
        f"**{col}** → Mean: {ci['mean']:.2f} | Range: ({ci['lower']:.2f}, {ci['upper']:.2f})"
    )

# ---------------- VISUALS ----------------
st.divider()
st.markdown("### 📈 Visual Insights")
for fig in plot_trends(df):
    st.pyplot(fig)

# ---------------- SMART INSIGHTS ----------------
st.divider()
st.markdown("### 🧠 Smart Insights")

if mode == "sales":
    from modes.sales.analysis import sales_insights
    insights = sales_insights(df, date_col=date_col, target_col=target_col)

    st.metric("Total Sales", insights.get("total_sales", 0))
    st.metric("Average Sales", insights.get("average_sales", 0))

elif mode == "stocks":
    from modes.stocks.analysis import stock_insights
    insights = stock_insights(df, buy_col=buy_col, current_col=current_col, qty_col=qty_col)

    st.metric("Total Investment", insights.get("total_investment", 0), help="Total invested capital")
    st.metric("Current Value", insights.get("current_value", 0), help="Current portfolio value")
    st.metric("Total P/L", insights.get("total_profit_loss", 0))
    st.metric("Volatility", insights.get("volatility", 0))

else:
    insights = None

# ---------------- FLAGS ----------------
st.divider()
st.markdown("### 🚩 Smart Alerts")

flags = generate_flags(mode, df, insights)

if flags:
    for flag in flags:
        st.warning(flag)
else:
    st.success("No alerts detected for the current data.")

# ---------------- STORYTELLING MODE ----------------
st.divider()
st.markdown("### 🧠 Data Story")

story = generate_story(
    mode=mode,
    comparisons=comparisons,
    flags=flags
)
st.info(story)

# ---------------- SUMMARY ----------------
st.divider()
st.markdown("### 🧾 AI Summary")
st.info(generate_summary(mode, df, stats, insights))

# ---------------- PREDICTION ----------------
if mode == "prediction":
    st.divider()
    st.markdown("### 🔮 Prediction")

    target = st.selectbox("Target column", df.select_dtypes(include="number").columns)
    horizon = st.slider("Forecast periods", 1, 52, 12)
    scenario = st.selectbox("Scenario", ["normal", "optimistic", "pessimistic"])

    from modes.prediction.forecast import forecast_values
    forecast = forecast_values(df, target, periods=horizon, scenario=scenario)

    st.line_chart(forecast)
    st.warning("Predictions are probabilistic, not guaranteed.")

# ---------------- ASK AI ----------------
st.divider()
st.markdown("### 🤖 Ask AI")

q = st.text_input("Ask about trends, risk, drops, or predictions")
if q:
    st.success(answer_question(mode, q, df, stats, insights))

# ---------------- EXPORT ----------------
st.divider()
st.markdown("### 📤 Export")

st.download_button(
    "Download Data CSV",
    df.to_csv(index=False),
    file_name="processed_data.csv",
)