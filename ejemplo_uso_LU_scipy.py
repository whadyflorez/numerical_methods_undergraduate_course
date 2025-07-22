import numpy as np
from scipy.linalg import lu

A=np.array([[2,1],[-1,3]])
B=np.array([5,5])

x=np.linalg.solve(A,B)

P,L,U=lu(A)