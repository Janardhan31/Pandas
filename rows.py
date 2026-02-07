# head() - shows top 5 rows of data
# head(n) - shows top n numbers of data

# Tail() - shows last 5 numbers of data
# tail(5) - shows last n numbers of data


import pandas as pd
df = pd.read_json('sample_Data.json')

print('top 10 rows : ')
print(df.head())

print('bottom 10 rows : ')
print(df.tail())

