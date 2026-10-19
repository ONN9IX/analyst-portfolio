# Marketing Analytics — Digital Campaigns 2024

## Задача
На учебных данных о рекламных кампаниях рассчитать CTR, CPC и показатели, необходимые для сравнения сегментов.

## Dataset
В репозитории: `data/google_ads_jan_2024.csv`.

Период: **01.01.2024–30.01.2024**.  
Наблюдений: **1 000**.

Это **синтетический учебный набор**. Даты 2024 года являются значениями CSV, а не доказанной историей рекламного кабинета. Точное происхождение этой версии файла неизвестно; сходный исходный датасет и ограничения описаны в [data/README.md](data/README.md).

## Рассчитанные показатели по учебному CSV
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

## Ограничения интерпретации
Поле `Acquisition_Cost` нельзя автоматически трактовать как CAC без количества привлечённых клиентов. Revenue отсутствует, поэтому ROAS не рассчитывается. `ROI` и `Conversion_Rate` уже заданы в синтетическом источнике; средневзвешенные значения — учебные описательные метрики, не доказанная эффективность реального бизнеса.

## Навыки
Pandas, data validation, marketing metrics, weighted averages, segmentation, корректная интерпретация ограничений данных.
