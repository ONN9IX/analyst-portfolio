-- Synthetic educational fixture: dates are intentionally 2025.
INSERT INTO customers VALUES
(1,'Alex Morgan','Consumer','Europe'),
(2,'Taylor Reed','Corporate','North America'),
(3,'Jordan Lee','Small Business','Asia Pacific'),
(4,'Casey Brown','Consumer','Europe'),
(5,'Sam Wilson','Corporate','North America'),
(6,'Robin Davis','Consumer','South America');

INSERT INTO products VALUES
(101,'Laptop Pro','Technology',700,1100),
(102,'Wireless Mouse','Technology',18,35),
(103,'Office Desk','Furniture',180,320),
(104,'Ergonomic Chair','Furniture',140,260),
(105,'Notebook Pack','Office Supplies',4,10),
(106,'Hoodie','Clothing & Accessories',22,55);

INSERT INTO orders VALUES
(1001,1,'2025-01-05','completed'),
(1002,2,'2025-01-11','completed'),
(1003,1,'2025-02-03','completed'),
(1004,3,'2025-02-15','completed'),
(1005,4,'2025-03-01','completed'),
(1006,2,'2025-03-17','completed'),
(1007,5,'2025-04-02','completed'),
(1008,1,'2025-04-19','completed'),
(1009,6,'2025-05-07','cancelled'),
(1010,3,'2025-05-22','completed'),
(1011,4,'2025-06-09','completed'),
(1012,5,'2025-06-21','completed');

INSERT INTO order_items VALUES
(1001,101,1,5),(1001,102,2,0),
(1002,103,2,10),(1002,105,10,0),
(1003,104,1,0),(1003,106,2,5),
(1004,101,1,0),(1004,105,5,0),
(1005,104,2,10),
(1006,102,8,5),(1006,105,20,0),
(1007,103,1,0),(1007,104,2,5),
(1008,101,1,10),(1008,102,3,0),
(1009,106,4,0),
(1010,103,2,5),(1010,105,15,0),
(1011,106,5,10),(1011,102,2,0),
(1012,101,2,5);

INSERT INTO payments
SELECT
    ROW_NUMBER() OVER (ORDER BY o.order_id) AS payment_id,
    o.order_id,
    CASE WHEN o.order_id % 3 = 0 THEN 'Bank Transfer'
         WHEN o.order_id % 2 = 0 THEN 'PayPal'
         ELSE 'Card' END AS payment_method,
    ROUND(SUM(oi.quantity * p.unit_price * (1 - oi.discount_pct / 100.0)), 2) AS amount
FROM orders o
JOIN order_items oi USING (order_id)
JOIN products p USING (product_id)
WHERE o.status = 'completed'
GROUP BY o.order_id;
