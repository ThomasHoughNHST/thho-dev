import re
import pandas as pd


data = [[1, 'HOUSTON TX 77055'], [2, 'HOUSTON TX 77253 3128'], [3, 'HOUSTON TX 77060 HD 99'],
        [4, 'HOUSTON TX 77002 HD079'], [5, 'HOUSTON TX 77060 6006 '], [6, 'NEW YORK NY 10017 1021 Y79'],
        [7, 'HOUSTON TX 77002 4995 HD079'], [8, 'KS'], [9, 'BIRMINGHAM AL 35201 143']]
address_history = pd.DataFrame(data=data, columns=['id', 'addressextension4'])
address_history['state_code'] = None
address_history['zip_code'] = None
address_history['city'] = None


pattern1 = '\\d{5}\\s{1}\\D{2}'
pattern2 = '\\w{4}\\s{1}\\d{5}\\s{1}\\D{2}'
pattern3 = '\\w{5}\\s{1}\\d{5}\\s{1}\\D{2}'
pattern4 = '\\w{2}\\s{1}\\w{2}\\s{1}\\d{5}\\s{1}\\D{2}'
pattern5 = '\\w{3}\\s{1}\\w{4}\\s{1}\\d{5}\\s{1}\\D{2}'
pattern6 = '\\w{5}\\s{1}\\w{4}\\s{1}\\d{5}\\s{1}\\D{2}'
pattern7 = '\\D{2}'
pattern8 = '\\w{3}\\s{1}\\d{5}\\s{1}\\D{2}'
for i, row in address_history.iterrows():
    a = str(row['addressextension4'])[::-1].strip()
    if re.match(pattern1, a):
        state_code = a[5:8]
        state_code = str(state_code)[::-1]
        zip_code = a[0:6]
        zip_code = str(zip_code)[::-1]
        city = a[9::]
        city = str(city)[::-1]
        address_history.at[i, 'state_code'] = state_code
        address_history.at[i, 'zip_code'] = zip_code
        address_history.at[i, 'city'] = city
    elif re.match(pattern2, a):
        state_code = a[10:13]
        state_code = str(state_code)[::-1]
        zip_code = a[5:11]
        zip_code = str(zip_code)[::-1]
        city = a[14::]
        city = str(city)[::-1]
        address_history.at[i, 'state_code'] = state_code
        address_history.at[i, 'zip_code'] = zip_code
        address_history.at[i, 'city'] = city
    elif re.match(pattern3, a) or re.match(pattern4, a):
        state_code = a[11:14]
        state_code = str(state_code)[::-1]
        zip_code = a[6:12]
        zip_code = str(zip_code)[::-1]
        city = a[15::]
        city = str(city)[::-1]
        address_history.at[i, 'state_code'] = state_code
        address_history.at[i, 'zip_code'] = zip_code
        address_history.at[i, 'city'] = city
    elif re.match(pattern5, a):
        state_code = a[14:17]
        state_code = str(state_code)[::-1]
        zip_code = a[9:15]
        zip_code = str(zip_code)[::-1]
        city = a[18::]
        city = str(city)[::-1]
        address_history.at[i, 'state_code'] = state_code
        address_history.at[i, 'zip_code'] = zip_code
        address_history.at[i, 'city'] = city
    elif re.match(pattern6, a):
        state_code = a[16:19]
        state_code = str(state_code)[::-1]
        zip_code = a[11:17]
        zip_code = str(zip_code)[::-1]
        city = a[20::]
        city = str(city)[::-1]
        address_history.at[i, 'state_code'] = state_code
        address_history.at[i, 'zip_code'] = zip_code
        address_history.at[i, 'city'] = city
    elif re.fullmatch(pattern7, a):
        address_history.at[i, 'state_code'] = row['addressextension4']
        address_history.at[i, 'zip_code'] = row['zip_code']
        address_history.at[i, 'city'] = row['city']
    elif re.match(pattern8, a):
        state_code = a[9:12]
        state_code = str(state_code)[::-1]
        zip_code = a[4:10]
        zip_code = str(zip_code)[::-1]
        city = a[13::]
        city = str(city)[::-1]
        address_history.at[i, 'state_code'] = state_code
        address_history.at[i, 'zip_code'] = zip_code
        address_history.at[i, 'city'] = city
    else:
        address_history.at[i, 'state_code'] = row['state_code']
        address_history.at[i, 'zip_code'] = row['zip_code']
        address_history.at[i, 'city'] = row['city']

print(address_history)
