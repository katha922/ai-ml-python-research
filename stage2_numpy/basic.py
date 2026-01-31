import numpy as np

array = [1,2,3,4]
list=array*2
print(list)

arr=np.array(array)
print(arr*2)

#1D array

a=np.array([1,2,3,4])
print(a)

#2D array

b=np.array([[1,2,3,4],
            [5,6,7,8]])
print(b)

#3D array

c=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(c)

print(np.zeros(5))
print(np.ones(5))
print(np.zeros((2, 3))) #2 row 3 column
print(np.ones((3, 2)))  #3 row 2 column
print(np.arange(1, 10)) #1-9
print(np.arange(1, 10, 2)) #1 3 5 7 9

arr = np.array([[1,2,3],[4,5,6]])
print('here')
print(arr.shape)
print(arr.size)
print(arr.dtype)

#indexing & slicing. In CSV, dataset cleaning its must need

arr = np.array([20, 30, 40, 50])
print(arr[0])     
print(arr[-1])
print(arr[1:3])   

mat = np.array([
    [1,2,3],
    [4,5,6]
])
print(mat[0,1]) #row-0 col-1
print(mat[:,1]) #all row col-1
print(mat[1,:]) #row-1

#type casting

arr = np.array([1.5, 2.7])
print(arr.astype(int))

arr2 = np.array([1,2,3])
print(arr2.astype(float))



