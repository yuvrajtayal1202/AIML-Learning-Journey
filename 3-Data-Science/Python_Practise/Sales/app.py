import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

sales = np.random.randint(1000, 5001, size = 12)


df = pd.DataFrame({
    'Months' : months,
    'Sales' : sales
})

max_month = df.loc[df['Sales'].idxmax()]
min_month = df.loc[df['Sales'].idxmin()]

print(f"Minimum Sales Month: {min_month}" )
print(f"Maximum Sales Month: {max_month}" )

colors =  ['red' if i == df['Sales'].max() else 'skyblue' for i in df['Sales']]

plt.figure(figsize=[10,6])
plt.bar(df['Months'], df['Sales'], color = colors)
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales {$}")
plt.grid(axis='y', linestyle='dashed', alpha=0.5)
plt.tight_layout()
plt.show()