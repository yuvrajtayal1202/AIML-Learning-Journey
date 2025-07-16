import pandas as pd

df = pd.DataFrame({
    "Name": ['Alice', 'Bob'],
    "Age": [3, 4],
})

print(df)
print(df['Age'])