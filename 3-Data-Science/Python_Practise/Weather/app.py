import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
temp = np.array([32,43,64,23,45,34,25])

df = pd.DataFrame({
    'Days' : days,
    'Temp' : temp
})
df['Status'] = ['Hot' if i > 40 else 'Mild' if i >= 25 else 'cold' for i in df['Temp']]
max_temp = np.max(df['Temp'])
min_temp = np.min(df['Temp'])
mean_temp = np.mean(df['Temp'])
print(max_temp)
print(min_temp)
print(mean_temp)

plt.figure(figsize=(10, 6))
plt.axhline(mean_temp, color='orange', linestyle='--', linewidth=1.5, label=f'Average ({mean_temp:.1f}°C)')
plt.axhline(max_temp, color='red', linestyle=':', linewidth=1.5, label=f'Max ({max_temp}°C)')
plt.axhline(min_temp, color='green', linestyle=':', linewidth=1.5, label=f'Min ({min_temp}°C)')

plt.plot(df['Days'], df['Temp'], marker='o', label='Daily Temp', color='royalblue')
plt.title('Temperature over Days')
plt.xlabel('Days')
plt.ylabel('Temperature C')
plt.grid(linestyle='dashed', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()