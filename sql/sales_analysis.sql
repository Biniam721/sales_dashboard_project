--total revenue and profit, total margin


WITH sales_data AS (
    SELECT
        order_id,
        round(sum(revenue), 2) AS total_revenue,
        round(sum(profit), 2) AS total_profit
    FROM sales
    GROUP BY order_id
)

SELECT 
    product,
    customer_name,
    region,
    date_trunc('month', order_date) AS month,
    total_revenue,
    total_profit,
    round((total_profit / total_revenue) * 100, 2) AS profit_margin_pct
FROM sales_data
INNER JOIN sales on sales.order_id = sales_data.order_id
ORDER BY total_revenue DESC
LIMIT 10;

-- top 5 products by revenue

SELECT
product,
SUM(revenue) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;

-- top 5 customers by revenue

SELECT
customer_name,
SUM(revenue) AS revenue
FROM sales
GROUP BY customer_name
ORDER BY revenue DESC
LIMIT 10;

-- Revenue by region

SELECT
region,
SUM(revenue) revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- monthy sales trend

SELECT
DATE_TRUNC('month',order_date) AS month,
SUM(revenue) revenue
FROM sales
GROUP BY month
ORDER BY month;
