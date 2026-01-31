import numpy as np

#matrix multiplication
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
print(A @ B)

w= np.random.randn(3,5)
x=np.random.randn(5,2)
print(w)
print(x)
print(w@x)

#trancepose

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.T)

I=np.eye(3)
print(I)
print(A)
print(A@I)

#determinant

A = np.array([[2, 1],
              [5, 3]])

det = np.linalg.det(A)
print(det)

if det == 0:
    print("Matrix is singular (no inverse)")
else:
    print("Matrix is invertible")

inverse = np.linalg.inv(A)
print(inverse)
