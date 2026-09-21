SELECT
    DATE_TRUNC('month', order_date)::date AS month,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(total_sales), 2) AS revenue
FROM ecommerce_sales
GROUP BY 1
ORDER BY 1;
