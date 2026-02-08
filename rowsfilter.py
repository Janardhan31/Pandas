import pandas as pd

data = {
    'name': ['ram','shyam','ghanshyam','dhanyshyam','aditi','jagdish','raj','simran'],
    'age': [17,23,22,65,34,55,24,63],
    'salary': [5777,45555,35555,87666,5677,8564,70000,34444],
    'performance_score': [75,77,97,44,58,38,88,66]
}

df= pd.DataFrame(data)

high_salary = df[df['salary']>50000]
print('employee with salary greater than 50000')
print(high_salary)


# filtering rows salary>50000 and age>30
filtered_rows = df[(df['salary']>50000)&(df['age']>30)]
print(filtered_rows)


# using or condition
filtered_or = df[(df['age']>35) | (df['performance_score']>90)]
print(filtered_or)