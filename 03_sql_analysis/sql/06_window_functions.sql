-- Olist: MoM и накопительная выручка
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', o.order_purchase_timestamp)::date AS month,
        SUM(oi.price) AS revenue
    FROM olist_orders o
    JOIN olist_order_items oi USING (order_id)
    WHERE o.order_status = 'delivered'
    GROUP BY 1
),
with_lag AS (
    SELECT
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY month) AS previous_month_revenue
    FROM monthly
)
SELECT
    month,
    ROUND(revenue::numeric, 2) AS revenue,
    ROUND(previous_month_revenue::numeric, 2) AS previous_month_revenue,
    ROUND(100.0 * (revenue - previous_month_revenue)
          / NULLIF(previous_month_revenue, 0), 2) AS mom_growth_pct,
    ROUND(SUM(revenue) OVER (ORDER BY month)::numeric, 2) AS cumulative_revenue
FROM with_lag
ORDER BY month;
