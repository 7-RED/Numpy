import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6],[3, 7, 9]])
arr2 = np.array([[2, 13], [14, 5],[7,3]])
arr3 = np.array([[11, -2, 3], [-4, 5, 6],[3, 7, -9]])

print(arr3.T)
newarr = np.dot(arr1, arr3.T)
print(newarr)

