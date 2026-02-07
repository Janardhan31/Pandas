import pandas as pd



df= pd.DataFrame(data)

print(df)

df.to_csv("output.csv", index=False)