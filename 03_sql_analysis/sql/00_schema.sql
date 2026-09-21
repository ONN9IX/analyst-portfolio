CREATE TABLE IF NOT EXISTS ecommerce_sales (
    order_id TEXT PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_name TEXT NOT NULL,
    customer_segment TEXT,
    country TEXT,
    region TEXT,
    product_category TEXT,
    product_name TEXT,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    unit_price NUMERIC(14,2) NOT NULL CHECK (unit_price >= 0),
    discount_percent NUMERIC(6,2),
    total_sales NUMERIC(14,2) NOT NULL CHECK (total_sales >= 0),
    shipping_cost NUMERIC(14,2),
    profit NUMERIC(14,2),
    payment_method TEXT
);
