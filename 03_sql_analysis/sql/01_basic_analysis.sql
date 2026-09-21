SELECT
    COUNT(DISTINCT order_id) AS orders,
    COUNT(DISTINCT customer_name) AS customers,
    SUM(quantity) AS units,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    ROUND(AVG(quantity * unit_price), 2) AS average_order_value
FROM ecommerce_sales;
