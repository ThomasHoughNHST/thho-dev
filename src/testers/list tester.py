import pandas as pd

data = [[23, '1987-12-05', 34, 667777, '2020-01-08'], [46, '1976-05-23', 69, 234, '2020-01-08'],
        [67, '1995-03-14', 87, 23556, '2020-01-08']]

ints = ['id', 'id_2', 'id_3']
dates = ['date', 'date_2']

df = pd.DataFrame(columns=['id', 'date', 'id_2', 'id_3', 'date_2'], data=data)
for i in ints:
    df[i] = pd.to_numeric(df[i], downcast='integer', errors='coerce')
for i in dates:
    df[i] = pd.to_datetime(df[i], format='%Y-%m-%d', errors='coerce')

print(df.dtypes)
print(df.head())
