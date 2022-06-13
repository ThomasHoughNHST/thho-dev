import pandas as pd
import numpy as np

publication = 'DN'

data = [
    [1, 'AVTALEGIRO', '2261-11-04', '2023-02-01'],
    [2, 'AVTALEGIRO', '2022-11-06', '2024-02-01'],
    [3, 'KREDITTKORTAVTALE', '2022-11-08', '2024-02-01'],
    [4, 'EFAKTURA', '2022-11-01', '2024-02-01']
]

subscription_with_price = pd.DataFrame(data=data,
                                       columns=['customer_number', 'payment_type', 'delivery_end_date', 'max_date'])
date_cols = ['delivery_end_date', 'max_date']
for i in date_cols:
    subscription_with_price[i] = pd.to_datetime(subscription_with_price[i], format='%Y-%m-%d', errors='coerce')

subscription_with_price['inv_date'] = None
subscription_with_price['day'] = subscription_with_price['delivery_end_date'].dt.day
print(subscription_with_price)
subscription_with_price['inv_date'] = np.where(
    subscription_with_price['payment_type'].str.contains('AVTALEGIRO'),
    subscription_with_price['delivery_end_date'] + pd.DateOffset(days=subscription_with_price['delivery_end_date'].dt.day),
    subscription_with_price['delivery_end_date'] + pd.DateOffset(days=10)
)
subscription_with_price = subscription_with_price[
    ['delivery_end_date', 'inv_date', 'day']
]
print(subscription_with_price)
