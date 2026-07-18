import pandas as pd
from modes.sales.analysis import sales_insights
from modes.stocks.analysis import stock_insights


def test_sales_insights_missing_target_column():
    df = pd.DataFrame({"Date": ["2024-01-01"], "Revenue": [100]})
    result = sales_insights(df, target_col="Sales")
    assert result == {}


def test_sales_insights_basic_calculation():
    df = pd.DataFrame({"Date": ["2024-01-01", "2024-01-02"], "Sales": [100, 150]})
    result = sales_insights(df, date_col="Date", target_col="Sales")
    assert result["total_sales"] == 250
    assert result["average_sales"] == 125
    assert result["growth_periods"] == 1


def test_stock_insights_missing_required_columns():
    df = pd.DataFrame({"Buy_Price": [10]})
    result = stock_insights(df)
    assert result == {}


def test_stock_insights_zero_investment_row_excluded():
    df = pd.DataFrame({
        "Buy_Price": [0, 10],
        "Current_Price": [5, 12],
        "Quantity": [1, 1],
    })
    result = stock_insights(df)
    assert result["excluded_rows"] == 1