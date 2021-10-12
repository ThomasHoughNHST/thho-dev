import re
import pandas as pd
from nhst_airflow import get_logger
logger = get_logger(__name__)


data = [[1, 'HOUSTON TX 77055'], [2, 'HOUSTON TX 77253 3128']]
df = pd.DataFrame(data=data, columns=['id', 'address'])
df['state_code'] = None
df['zip'] = None


pattern1 = '\\d{5}\\s{1}\\D{2}'
pattern2 = '\\w{4}\\s{1}\\d{5}\\s{1}\\D{2}'
for i, row in df.iterrows():
    a = str(row['address'])[::-1]
    if re.match(pattern1, a):
        state_code = a[5:8]
        state_code = str(state_code)[::-1]
        zip_code = a[0:6]
        zip_code = str(zip_code)[::-1]
        logger.info(state_code)
        df.at[i, 'state_code'] = state_code
        df.at[i, 'zip'] = zip_code
    elif re.match(pattern2, a):
        state_code = a[10:13]
        state_code = str(state_code)[::-1]
        zip_code = a[5:11]
        zip_code = str(zip_code)[::-1]
        logger.info(state_code)
        df.at[i, 'state_code'] = state_code
        df.at[i, 'zip'] = zip_code
    else:
        df.at[i, 'state_code'] = row['state_code']
        df.at[i, 'zip'] = row['zip']

logger.info(df)



