# Yandex DataLens Dashboard — спецификация

## Датасет
`E-commerce Sales 2023–2025`

## KPI
Верхний блок:
- Revenue
- Profit
- Orders
- Customers
- Units Sold
- AOV
- Profit Margin

## Основные чарты
1. Revenue by Month — динамика выручки во времени.
2. Revenue by Category — сравнение товарных категорий.
3. Revenue by Region — географическое распределение выручки.
4. Revenue by Customer Segment — сравнение клиентских сегментов.
5. Profit Margin by Category — сравнение маржинальности категорий.
6. Top Products by Revenue — товары с наибольшей выручкой.

## Селекторы
- Region
- Product_Category
- Customer_Segment
- Order_Date

Селекторы применяются к KPI и аналитическим чартам.

## Контрольные значения без фильтров
| KPI | Значение |
|---|---:|
| Revenue | 484 559,34 |
| Profit | 158 872,32 |
| Orders | 2 000 |
| Customers | 1 534 |
| Units Sold | 7 115 |
| AOV | 242,28 |
| Profit Margin | 32,79% |

## Контроль фильтрации
- Region = Europe → Revenue 137 006,20
- Product_Category = Furniture → Revenue 256 274,68

## Принцип
KPI рассчитываются из полей датасета и не вводятся вручную. Значения сверяются с Python-анализом того же CSV.
