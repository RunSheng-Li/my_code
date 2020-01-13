import numpy as np

A = np.random.random((4, 4))
print(A)
print(A < 0.5)
print(A[A < 0.5])
