import pandas as pd


# read json file
df = pd.read_json('sample_Data.json')

print('dispalying the info of data set')
print(df.info())
