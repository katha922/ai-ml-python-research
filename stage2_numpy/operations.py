import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a*b)
print(a**2)

#broadcasting

x=np.array([[1],[2]])
print(x.shape)

y=np.array([[1,2,3],[4,5,6]])
print(y.shape)

print(x+y)

#reshape

array = np.arange(1,13)
array = array.reshape(2,6)
print(array)

arr = np.array([1,4,9,16])

print(np.sqrt(arr))
print(np.log(arr))
print(np.exp(arr))

data = np.array([10,20,30])

print(np.sum(data))
print(np.mean(data))
print(np.min(data))
print(np.max(data))

#axis

mat = np.array([[1,2,3],[4,5,6]])

print(np.sum(mat, axis=0))  # column wise
print(np.sum(mat, axis=1))  # row wise

#Statistical Functions
data = np.array([10,20,30,40])

print(np.std(data)) #Std = √variance
print(np.var(data)) #variance = average of (value - mean)²
