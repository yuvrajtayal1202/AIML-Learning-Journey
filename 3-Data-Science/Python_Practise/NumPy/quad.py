import matplotlib.pyplot as plt

x = list(range(0,11))
y = [i**2 for i in x]

plt.plot(x, y, marker='o')

plt.xlabel('x Values')
plt.ylabel('y = x^2')

plt.title('Quadratic functions')

plt.grid(True)
plt.show()