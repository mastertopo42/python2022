#Транспонируйте матрицу из предыдущего пункта
import numpy as np


array1 = np.array([i for i in range(1, 100, 3)])
array2 = np.array([i for i in range(2, 100, 3)])
array3 = np.array([i for i in range(3, 100, 3)])
arr = (array1 + array2 + array3)
matrix = arr.reshape(11,3)
print(matrix.T)




