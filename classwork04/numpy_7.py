# Запишите срез матрицы из пункта 5 в файл matrix.dat.
# Срез должен включать в себя 1, 5, 9 столбцы и 0 и 2 строки.
# Подсказка: требуется вписать элементы матрицы, которая состоит из пересечения соответсвующих столбцов и строк.
import numpy as np

array1 = np.array([i for i in range(1, 100, 3)])
array2 = np.array([i for i in range(2, 100, 3)])
array3 = np.array([i for i in range(3, 100, 3)])
arr = (array1 + array2 + array3)
matrix = arr.reshape(11,3)
#print(matrix.T)

print(matrix.T[::2, ::4], "\n")

