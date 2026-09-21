# Данные

Проект использует **Brazilian E-Commerce Public Dataset by Olist** — реальные анонимизированные данные примерно о 100 тыс. заказов за 2016–2018 годы.

Нужные таблицы:
- olist_customers_dataset.csv
- olist_orders_dataset.csv
- olist_order_items_dataset.csv
- olist_products_dataset.csv
- product_category_name_translation.csv

Исходные CSV не дублируются в репозитории: источник — Kaggle, *Brazilian E-Commerce Public Dataset by Olist*.

Важно: для анализа повторных покупок используется `customer_unique_id`, а не `customer_id`.
