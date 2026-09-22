# E-commerce 360 — итоговый проект Data Analyst

## Цель
End-to-end анализ e-commerce данных **2023–2025**: проверка качества → Python → SQL-логика → бизнес-KPI → подготовка данных для BI.

## Dataset
`data/global_ecommerce_sales.csv` — 2 000 заказов, 02.01.2023–31.12.2025.

## Проверенные KPI
| Метрика | Значение |
|---|---:|
| Orders | 2 000 |
| Customers | 1 534 |
| Units | 7 115 |
| Revenue | 484 559.34 |
| Profit | 158 872.32 |
| Profit Margin | 32.79% |
| AOV | 242.28 |
| Shipping Cost | 25 804.24 |
| Repeat Customer Rate | 25.55% |

## Категории
| Category | Revenue | Profit | Margin |
|---|---:|---:|---:|
| Furniture | 256 274.68 | 81 171.57 | 31.67% |
| Technology | 139 518.22 | 48 268.65 | 34.60% |
| Clothing & Accessories | 69 375.63 | 26 112.94 | 37.64% |
| Office Supplies | 19 390.81 | 3 319.16 | 17.12% |

## Наблюдения
Furniture формирует наибольшую выручку. Clothing & Accessories имеет наиболее высокую profit margin среди четырёх категорий, а Office Supplies — наиболее низкую. Repeat Customer Rate по имени клиента составляет 25.55%.

## Ограничения
`Customer_Name` используется как доступный идентификатор клиента; это слабее стабильного `customer_id`, поэтому repeat rate следует трактовать как показатель внутри данного учебного набора. Причинные выводы из наблюдательных данных не делаются.

## Воспроизводимость
```bash
pip install -r requirements.txt
python analysis.py
```

Скрипт формирует CSV в `results/`: KPI, месячную динамику, категории, регионы и клиентов.

## Навыки
Python, Pandas, data quality, KPI, customer analysis, time-series aggregation, business interpretation, подготовка данных для BI.
