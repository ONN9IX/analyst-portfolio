-- 1. Monthly sales
SELECT
    DATE_TRUNC('month', o.order_date)::date AS month,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(SUM(oi.quantity * p.unit_price * (1 - oi.discount_pct / 100.0)), 2) AS revenue
FROM orders o
JOIN order_items oi USING (order_id)
JOIN products p USING (product_id)
WHERE o.status = 'completed'
GROUP BY 1
ORDER BY 1;

-- 2. Category economics
SELECT
    p.category,
    ROUND(SUM(oi.quantity * p.unit_price * (1 - oi.discount_pct / 100.0)), 2) AS revenue,
    ROUND(SUM(oi.quantity * (p.unit_price * (1 - oi.discount_pct / 100.0) - p.unit_cost)), 2) AS gross_profit
FROM orders o
JOIN order_items oi USING (order_id)
JOIN products p USING (product_id)
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY revenue DESC;

-- 3. Customer metrics + CASE segmentation
WITH customer_metrics AS (
    SELECT
        c.customer_id,
        c.customer_name,
        COUNT(DISTINCT o.order_id) FILTER (WHERE o.status = 'completed') AS completed_orders,
        COALESCE(SUM(oi.quantity * p.unit_price * (1 - oi.discount_pct / 100.0))
                 FILTER (WHERE o.status = 'completed'), 0) AS revenue
    FROM customers c
    LEFT JOIN orders o ON o.customer_id = c.customer_id
    LEFT JOIN order_items oi ON oi.order_id = o.order_id
    LEFT JOIN products p ON p.product_id = oi.product_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT
    customer_name,
    completed_orders,
    ROUND(revenue, 2) AS revenue,
    CASE
        WHEN revenue >= 2000 THEN 'High value'
        WHEN revenue >= 1000 THEN 'Medium value'
        ELSE 'Low value'
    END AS value_segment,
    CASE WHEN completed_orders > 1 THEN 'Repeat' ELSE 'One-time' END AS customer_type
FROM customer_metrics
ORDER BY revenue DESC;

-- 4. Top products inside each category
WITH product_sales AS (
    SELECT
        p.category,
        p.product_name,
        SUM(oi.quantity * p.unit_price * (1 - oi.discount_pct / 100.0)) AS revenue
    FROM orders o
    JOIN order_items oi USING (order_id)
    JOIN products p USING (product_id)
    WHERE o.status = 'completed'
    GROUP BY p.category, p.product_name
),
ranked AS (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY category ORDER BY revenue DESC) AS revenue_rank
    FROM product_sales
)
SELECT category, product_name, ROUND(revenue, 2) AS revenue, revenue_rank
FROM ranked
WHERE revenue_rank <= 2
ORDER BY category, revenue_rank;

-- 5. MoM and cumulative revenue
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', o.order_date)::date AS month,
        SUM(oi.quantity * p.unit_price * (1 - oi.discount_pct / 100.0)) AS revenue
    FROM orders o
    JOIN order_items oi USING (order_id)
    JOIN products p USING (product_id)
    WHERE o.status = 'completed'
    GROUP BY 1
),
lagged AS (
    SELECT month, revenue, LAG(revenue) OVER (ORDER BY month) AS prev_revenue
    FROM monthly
)
SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(100 * (revenue - prev_revenue) / NULLIF(prev_revenue, 0), 2) AS mom_pct,
    ROUND(SUM(revenue) OVER (ORDER BY month), 2) AS cumulative_revenue
FROM lagged
ORDER BY month;

-- 6. Payment mix
SELECT
    p.payment_method,
    COUNT(*) AS payments,
    ROUND(SUM(p.amount), 2) AS revenue,
    ROUND(100 * SUM(p.amount) / NULLIF(SUM(SUM(p.amount)) OVER (), 0), 2) AS revenue_share_pct
FROM payments p
GROUP BY p.payment_method
ORDER BY revenue DESC;
