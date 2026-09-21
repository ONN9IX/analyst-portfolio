-- Olist: базовые KPI по доставленным заказам
SELECT COUNT(*) AS delivered_orders
FROM olist_orders
WHERE order_status = 'delivered';

SELECT COUNT(DISTINCT customer_unique_id) AS unique_customers
FROM olist_orders o
JOIN olist_customers c USING (customer_id)
WHERE o.order_status = 'delivered';

SELECT ROUND(SUM(oi.price)::numeric, 2) AS product_revenue
FROM olist_order_items oi
JOIN olist_orders o USING (order_id)
WHERE o.order_status = 'delivered';

SELECT ROUND(
    SUM(oi.price)::numeric / NULLIF(COUNT(DISTINCT o.order_id), 0), 2
) AS average_order_value
FROM olist_order_items oi
JOIN olist_orders o USING (order_id)
WHERE o.order_status = 'delivered';
