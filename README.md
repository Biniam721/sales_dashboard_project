# 📊 Sales Performance Dashboard

## Overview

This project is an interactive Sales Performance Dashboard built using Python, Pandas, Plotly, and Streamlit. The dashboard provides insights into revenue, profit, product performance, customer behavior, and regional sales trends.

The goal of this project is to transform raw sales data into actionable business insights that support data-driven decision-making.

---

## Business Problem

Organizations need a clear view of their sales performance to identify growth opportunities, monitor profitability, and understand customer purchasing patterns.

This dashboard answers key business questions:

- What is the total revenue and profit?
- Which products generate the highest revenue?
- Which regions perform best?
- How do sales change over time?
- Who are the top customers?
- What categories contribute most to revenue?

---

## Dataset

The dataset contains sales transactions with the following fields:

| Column | Description |
|----------|----------|
| Order_ID | Unique order identifier |
| Order_Date | Date of order |
| Customer_Name | Customer name |
| Region | Sales region |
| Product | Product sold |
| Category | Product category |
| Quantity | Quantity sold |
| Unit_Price | Price per unit |
| Revenue | Total sales amount |
| Cost | Total cost |
| Profit | Revenue - Cost |

---

## Technologies Used

- Python
- Pandas
- Plotly
- Streamlit
- PostgreSQL
- SQL
- Git & GitHub

---

## Dashboard Features

### KPI Cards

- Total Revenue
- Total Profit
- Profit Margin
- Total Orders
- Average Order Value

### Interactive Visualizations

- Revenue by Region
- Monthly Revenue Trend
- Revenue by Product
- Revenue by Category
- Top Customers Analysis

### Filters

- Region Filter
- Date Range Filter

---

## SQL Analysis

Example KPIs calculated using SQL:

### Total Revenue

```sql
SELECT SUM(revenue)
FROM sales;
```

### Total Profit

```sql
SELECT SUM(profit)
FROM sales;
```

### Revenue by Region

```sql
SELECT
    region,
    SUM(revenue) revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;
```

### Top Products

```sql
SELECT
    product,
    SUM(revenue) revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
```

---

## Key Insights

- Identified the highest-performing sales regions.
- Analyzed revenue trends across different months.
- Determined the most profitable products.
- Evaluated customer purchasing behavior.
- Measured overall business profitability.

---

## Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- SQL Querying
- Data Visualization
- KPI Development
- Dashboard Design
- Business Intelligence Reporting
- Data Storytelling

---

## How to Run the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/sales-dashboard.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
streamlit run dashboard.py
```

---

## Future Improvements

- Connect directly to PostgreSQL database
- Add forecasting models for future sales
- Deploy dashboard to Streamlit Cloud
- Add customer segmentation analysis
- Add advanced business KPIs

---

## Author

**Biniam Tekeste**

Aspiring Data Analyst with expertise in SQL, Python, Data Visualization, and Business Intelligence.

LinkedIn: www.linkedin.com/in/biniam-tekeste-646599268

Email: btekeste532@gmail.com