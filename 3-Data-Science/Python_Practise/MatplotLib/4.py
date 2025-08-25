import numpy as np
import matplotlib.pyplot as plt

# Generate 10 random x and y values between 0 and 1
x = np.random.rand(100)

plt.hist (x, bins=100, color='purple', edgecolor='black')
plt.show()