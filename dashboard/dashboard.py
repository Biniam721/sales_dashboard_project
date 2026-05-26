import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

# Load Data
df = pd.read_csv("/Users/bina/Movies/sales_dashboard_project/data/sales_dashboard_dataset.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# =========================
# KPIs
# =========================

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()

profit_margin = (
    total_profit / total_revenue
) * 100

st.title("📊 Sales Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", f"${total_revenue:,.0f}")
col2.metric("Profit", f"${total_profit:,.0f}")
col3.metric("Orders", total_orders)
col4.metric("Margin", f"{profit_margin:.2f}%")

avg_order_value = total_revenue / total_orders

top_product = (
    df.groupby("Product")["Revenue"]
      .sum()
      .idxmax()
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Order Value",
    f"${avg_order_value:,.0f}"
)

col2.metric(
    "Top Product",
    top_product
)

col3.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)

# =========================
# Revenue by Region
# =========================

region_sales = (
    df.groupby("Region")["Revenue"]
      .sum()
      .reset_index()
)

fig_region = px.bar(
    region_sales,
    x="Region",
    y="Revenue",
    title="Revenue by Region"
)

st.plotly_chart(fig_region, use_container_width=True)

# =========================
# Monthly Trend
# =========================

monthly_sales = (
    df.groupby(
        df["Order_Date"].dt.to_period("M")
    )["Revenue"]
    .sum()
    .reset_index()
)

monthly_sales["Order_Date"] = (
    monthly_sales["Order_Date"]
    .astype(str)
)

fig_month = px.line(
    monthly_sales,
    x="Order_Date",
    y="Revenue",
    markers=True,
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig_month, use_container_width=True)

# =========================
# Product Revenue
# =========================

product_sales = (
    df.groupby("Product")["Revenue"]
      .sum()
      .reset_index()
      .sort_values("Revenue", ascending=False)
)

fig_product = px.bar(
    product_sales,
    x="Product",
    y="Revenue",
    title="Top Products"
)

st.plotly_chart(fig_product, use_container_width=True)

# =========================
# Category Pie Chart
# =========================

category_sales = (
    df.groupby("Category")["Revenue"]
      .sum()
      .reset_index()
)

fig_pie = px.pie(
    category_sales,
    names="Category",
    values="Revenue",
    title="Revenue by Category"
)

st.plotly_chart(fig_pie, use_container_width=True)

# =========================
# Top Customers
# =========================

top_customers = (
    df.groupby("Customer_Name")["Revenue"]
      .sum()
      .reset_index()
      .sort_values("Revenue", ascending=False)
)

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

if selected_region != "All":
    df = df[df["Region"] == selected_region]

st.sidebar.header("Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    df["Order_Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["Order_Date"].max()
)

df = df[
    (df["Order_Date"] >= pd.to_datetime(start_date))
    & (df["Order_Date"] <= pd.to_datetime(end_date))
]

st.subheader("Top Customers")
st.dataframe(top_customers)

st.subheader("Business Insights")

st.write(
    f"""
    - Total Revenue: ${total_revenue:,.0f}
    - Total Profit: ${total_profit:,.0f}
    - Top Product: {top_product}
    - Profit Margin: {profit_margin:.2f}%
    """
)