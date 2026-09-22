# Вычисляемые поля Yandex DataLens

Датасет: `E-commerce Sales 2023–2025`

| Поле | Формула |
|---|---|
| Revenue | `SUM([Total_Sales])` |
| Total Profit | `SUM([Profit])` |
| Orders | `COUNTD([Order_ID])` |
| Customers | `COUNTD([Customer_Name])` |
| Units Sold | `SUM([Quantity])` |
| AOV | `SUM([Total_Sales]) / COUNTD([Order_ID])` |
| Profit Margin | `SUM([Profit]) / SUM([Total_Sales])` |

## Проверка
На полном датасете:
- Revenue: 484 559,34
- Total Profit: 158 872,32
- Orders: 2 000
- Customers: 1 534
- Units Sold: 7 115
- AOV: 242,28
- Profit Margin: 32,79%

`Customers` использует Customer_Name из-за отсутствия Customer_ID в исходном наборе.
