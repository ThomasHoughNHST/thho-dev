import pandas as pd

data = [[1, 'A'], [2, 'B'], [3, 'C']]
data2 = [[1, 'A1'], [2, 'B'], [3, 'C']]
df = pd.DataFrame(data, columns=['id', 'letter'])
df2 = pd.DataFrame(data, columns=['id', 'letter'])
o = df.equals(df2)
print(o)

out = pd.merge(df, df2,
               indicator=True,
               how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
print(out)
