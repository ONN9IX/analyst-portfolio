# Marketing Analytics — Digital Campaigns 2024

## Задача
Проанализировать эффективность digital-кампаний по данным января 2024 года и показать расчёт маркетинговых KPI без выдуманных метрик.

## Dataset
В репозитории: `data/google_ads_jan_2024.csv`.

Период: **01.01.2024–30.01.2024**.  
Наблюдений: **1 000**.

Источник проекта прямо указывает, что данные извлекались через **Mockaroo**, то есть это **синтетические учебные данные**, имитирующие выгрузку рекламных API. Это явно отмечено и не выдаётся за реальные рекламные транзакции.

## Проверенные агрегаты
| Метрика | Значение |
|---|---:|
| Campaign rows | 1 000 |
| Impressions | 10 785 810 |
| Clicks | 1 027 999 |
| CTR | 9.53% |
| Acquisition Cost | 12 283 827.89 |
| CPC | 11.95 |
| Cost-weighted ROI field | 4.97 |
| Click-weighted Conversion Rate | 8.04% |

## Что анализируем
- CTR = Clicks / Impressions;
- CPC = Acquisition Cost / Clicks;
- Conversion Rate — поле источника;
- ROI — поле источника;
- Campaign Type, audience, location, customer segment.

## Важное ограничение
Поле `Acquisition_Cost` нельзя автоматически трактовать как CAC без количества реально привлечённых клиентов. Поэтому проект **не подменяет Acquisition Cost метрикой CAC**. Аналогично revenue отсутствует, поэтому ROAS из этого набора не рассчитывается.

## Навыки
Pandas, data validation, marketing metrics, weighted averages, segmentation, корректная интерпретация ограничений данных.
