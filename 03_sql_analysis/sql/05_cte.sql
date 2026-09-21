WITH customer_sales AS (
    SELECT customer_name, SUM(quantity * unit_price) AS revenue
    FROM ecommerce_sales
    GROUP BY customer_name
)
SELECT customer_name, ROUND(revenue, 2) AS revenue
FROM customer_sales
WHERE revenue > (SELECT AVG(revenue) FROM customer_sales)
ORDER BY revenue DESC;
