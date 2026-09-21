WITH customer_sales AS (
    SELECT o.customer_id, SUM(oi.total_amount) AS revenue
    FROM orders o
    JOIN order_items oi USING (order_id)
    GROUP BY o.customer_id
)
SELECT customer_id, ROUND(revenue, 2) AS revenue
FROM customer_sales
WHERE revenue > (SELECT AVG(revenue) FROM customer_sales)
ORDER BY revenue DESC;
