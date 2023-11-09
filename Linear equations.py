import numpy as np


A=np.array([[1,1,1],[0,2,5],[2,5,-1]])
B=np.array([[6],[-4],[27]])

X=np.dot(np.linalg.inv(A),B)
print(f'X is {X[0]}, y is {X[1]}, z is {X[2]}')

xx = np.linalg.solve(A, B)