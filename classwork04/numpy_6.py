#Произведите векторное умножение матрицы из предыдущего пункта на вектор размерности 11 из элементов от -9 до -1
import numpy as np

vector = np.array([i for i  in range(-9, 2)])

array1 = np.array([i for i in range(1, 100, 3)])
array2 = np.array([i for i in range(2, 100, 3)])
array3 = np.array([i for i in range(3, 100, 3)])
arr = (array1 + array2 + array3)
matrix = arr.reshape(11,3)
#print(matrix.T)

print(vector.T @ matrix)
