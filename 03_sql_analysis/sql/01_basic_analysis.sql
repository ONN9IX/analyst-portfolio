-- Базовые KPI интернет-магазина
SELECT COUNT(DISTINCT order_id) AS orders FROM orders;
SELECT COUNT(DISTINCT customer_id) AS customers FROM orders;
SELECT SUM(quantity * price) AS revenue FROM order_items;

SELECT
    SUM(oi.quantity * oi.price) / NULLIF(COUNT(DISTINCT o.order_id), 0) AS average_order_value
FROM orders o
JOIN order_items oi USING (order_id);
