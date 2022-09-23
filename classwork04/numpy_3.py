#Посчитайте сумму троек элементов из предыдущего пункта
import numpy as np

array1 = np.array([i for i in range(1, 100, 3)])
array2 = np.array([i for i in range(2, 100, 3)])
array3 = np.array([i for i in range(3, 100, 3)])
print (array1 + array2 + array3)



