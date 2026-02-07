# Step - 1 sample data set

import pandas as pd

data = {
    'name': ['ram','shyam','ghanshyam','dhanyshyam','aditi','jagdish','raj','simran'],
    'age': [17,23,22,65,34,55,24,63],
    'salary': [5777,45555,35555,87666,5677,8564,70000,34444],
    'performance score': [75,77,97,44,58,38,88,66]
}

df = pd.DataFrame(data)

print(df)
print('data description')
print(df.describe())