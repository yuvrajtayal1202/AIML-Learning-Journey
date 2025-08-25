import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

days = 100
price = 100
prices = []

for _ in range(1, days +1):
    price += np.random.rand()
    prices.append(price)


df = pd.DataFrame({
    'Day': np.arange(1, days + 1),
    'Price': prices
})
print(df)

df['7-Day Avg'] = df['Price'].rolling(window=7).mean()
df['30-Day Avg'] = df['Price'].rolling(window=30).mean()

max_price_day = df.loc[df['Price'].idxmax()]
print("Day with highest price:")
print(max_price_day)

plt.figure(figsize=(12, 6))
plt.plot(df['Day'], df['Price'], label='Price', color='blue')
plt.plot(df['Day'], df['7-Day Avg'], label='7-Day Avg', color='orange')
plt.plot(df['Day'], df['30-Day Avg'], label='30-Day Avg', color='green')

plt.title('Stock Price Simulation')
plt.xlabel('Day')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()
