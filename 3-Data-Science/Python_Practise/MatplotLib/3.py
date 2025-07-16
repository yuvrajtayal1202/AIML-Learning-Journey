import numpy as np
import matplotlib.pyplot as plt

# Generate 10 random x and y values between 0 and 1
x = np.random.rand(10)
y = np.random.rand(10)

# Create a scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Add title and axis labels
plt.title("Scatter Plot of 10 Random Points")
plt.xlabel("x values")
plt.ylabel("y values")
plt.grid(True)

# Show the plot
plt.show()
