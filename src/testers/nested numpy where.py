import pandas as pd
import numpy as np

data = [[223311, 'JA'], [554433, None], [334455, 'NEI']]

final_year_of_study = pd.DataFrame(data=data, columns=['customer_number', 'value'])

final_year_of_study['value'] = np.where(
    final_year_of_study['value'] == 'JA',
    'YES',
    np.where(
        final_year_of_study['value'] == 'NEI',
        'NO',
        final_year_of_study['value']
    )
)

print(final_year_of_study)
