import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])


last_two_rows = np.take(a, [-2,-1], axis=0)
print(last_two_rows)