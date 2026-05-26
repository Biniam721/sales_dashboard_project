\COPY sales FROM '/Users/bina/Movies/sales_dashboard_project/data/sales_dashboard_dataset.csv' DELIMITER ',' CSV HEADER;

SELECT *
FROM sales
LIMIT 5;