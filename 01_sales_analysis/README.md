# Анализ продаж — Global E-Commerce 2023–2025

## Цель
Воспроизводимый анализ современных e-commerce продаж: динамика, категории, товары, клиентские сегменты и география.

## Данные
Выбран публичный **Global E-Commerce Sales & Customer Analytics**:
- 2 000 заказов;
- период: **2023-01-01 — 2025-12-31**;
- 20 стран;
- поля включают Order_ID, Order_Date, Customer_Name, Customer_Segment, Country, Region, Product_Category, Product_Name, Quantity, Unit_Price.

Источник: Kaggle, `global_ecommerce_sales.csv`.

> Набор используется как публичный портфельный dataset. Он не заявляется как выгрузка конкретного магазина, если автор источника этого не подтверждает.

## Анализ
1. Проверка схемы, дат и дубликатов.
2. Revenue = Quantity × Unit_Price.
3. Orders, Customers, Units, AOV.
4. Месячная динамика.
5. Категории и товары.
6. Сегменты, страны и регионы.
7. Фактические выводы только после выполнения расчётов.

## Запуск
```bash
pip install -r requirements.txt
python analysis.py
```

Ожидаемый файл: `data/global_ecommerce_sales.csv`.
