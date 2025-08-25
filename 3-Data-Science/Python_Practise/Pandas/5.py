import pandas as pd

df = pd.DataFrame({
    "Name": ['Alice', 'Bob'],
    "Age": [3, 4]
})

df['Salary'] = [30000, 20000]

print(df['Age'].mean())