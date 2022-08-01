import pandas as pd
import numpy as np


def merge_duplicates(input_dataframe, join_key):
    step1 = pd.merge(input_dataframe, input_dataframe, how='inner',
                     on=[join_key, 'product', 'term', 'copies'])
    step1 = step1[
        step1['row_number_y'] > step1['row_number_x']]
    step1a = step1.groupby([join_key, 'row_number_x'])['row_number_y'].max()
    step1 = pd.merge(step1, step1a, on=[join_key, 'row_number_x'],
                     how='inner')[
        [join_key, 'row_number_x', 'row_number_y_y']
    ]
    step1.rename(columns={'row_number_x': 'row_number',
                          'row_number_y_y': 'row_number_new'},
                 inplace=True)
    step1 = step1.drop_duplicates()
    step2 = pd.merge(input_dataframe, input_dataframe, how='left', on=join_key)
    step2 = step2[
        (step2['row_number_y'] > step2['row_number_x']) &
        ((step2['product_x'] != step2['product_y']) |
         (step2['term_x'] != step2['term_y']) |
         (step2['copies_x'] != step2['copies_y']))
        ]
    step2a = step2.groupby([join_key, 'row_number_x'])['row_number_y'].min()
    step2 = pd.merge(step2, step2a, on=[join_key, 'row_number_x'], how='inner')[
        [join_key, 'row_number_x', 'row_number_y_y']
    ]
    step2['row_number_y_y'] = step2['row_number_y_y'] - 1
    step2.rename(columns={'row_number_x': 'row_number',
                          'row_number_y_y': 'row_number_new'},
                 inplace=True)
    step2 = step2.drop_duplicates()
    print(step2)
    step3 = pd.merge(input_dataframe, step1,
                     how='left',
                     on=[join_key, 'row_number'])
    step3 = pd.merge(step3, step2,
                     how='left',
                     on=[join_key, 'row_number'])
    step3['row_number_new'] = np.where((step3.row_number_new_y.notnull()),
                                       step3['row_number_new_y'],
                                       np.where((step3.row_number_new_x.notnull()),
                                                step3['row_number_new_x'],
                                                step3['row_number']))
    step3 = step3[[join_key, 'row_number', 'row_number_new']]
    step4 = step3[[join_key, 'row_number', 'row_number_new']]
    step4['row_number_2'] = step4.groupby([join_key, 'row_number_new'])['row_number'].rank(method='first')

    step5 = pd.merge(input_dataframe, step4,
                     how='inner',
                     on=[join_key, 'row_number'])[
        [join_key, 'valid_from_date', 'product', 'term',
         'copies', 'row_number_2']
    ]
    step5 = step5[step5['row_number_2'] == 1]
    step5['row_number_1'] = \
        step5.groupby([join_key])['valid_from_date'].rank(method='first')
    return step5


pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)
data = [
    [1, '2010-01-01', '2010-05-01', 'D6', '12', 2],
    [1, '2010-05-02', '2014-12-31', 'D6', '12', 2],
    [1, '2015-01-01', '2018-12-31', 'D6', '12', 2],
    [1, '2019-01-01', '2020-12-31', 'K6O', '12', 2],
    [1, '2021-01-01', '2021-04-30', 'K6O', '12', 2],
    [1, '2021-05-01', '2021-06-30', 'K6O', '06', 2],
    [1, '2021-07-01', '2021-07-31', 'K6O', '06', 3],
    [1, '2021-08-01', '2021-09-30', 'K6O', '06', 3],
    [2, '2021-08-01', '2021-09-30', 'K6O', '06', 3],
    [2, '2021-10-01', '2021-12-31', 'K6O', '06', 3],
    [2, '2022-01-01', '2022-12-31', 'K6O', '06', 3]
]
df = pd.DataFrame(data=data, columns=['customer_id', 'valid_from_date', 'valid_to_date', 'product', 'term', 'copies'])
df['valid_from_date'] = pd.to_datetime(df['valid_from_date'])
df['valid_to_date'] = pd.to_datetime(df['valid_to_date'])
df['row_number'] = df.groupby('customer_id')['valid_from_date'].rank(method='first')
df['customer_id'] = pd.to_numeric(df['customer_id'], downcast='integer')
df['copies'] = pd.to_numeric(df['copies'], downcast='integer')
df['row_number'] = pd.to_numeric(df['row_number'], downcast='integer')
df = merge_duplicates(input_dataframe=df, join_key='customer_id')




