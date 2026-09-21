SELECT
    customer_name,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM ecommerce_sales
GROUP BY customer_name
ORDER BY revenue DESC
LIMIT 20;
