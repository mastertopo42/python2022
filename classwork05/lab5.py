import numpy as np

np.random.seed(1)
array1 = np.random.random(120)  #генерируем массив из случайных чисел
mean1 = array1.mean()
std2 = array1.std()
sum1 = array1.sum()
array2 = array1.reshape(12, 10)  #превращаем в двумерный
sum2_0 = array2.sum(axis=0)
mean2_0 = array2.mean(axis=0)
std2_0 = array2.std(axis=0)
sum2_1 = array2.sum(axis=1)
mean2_1 = array2.mean(axis=1)
std2_1 = array2.std(axis=1)
min_0 = array2.min(axis=0)
min_1 = array2.min(axis=1)
max_0 = array2.max(axis=0)
max_1 = array2.max(axis=1)
ind_min_0 = array2.argmin(axis=0)
ind_min_1 = array2.argmin(axis=1)
ind_max_0 = array2.argmax(axis=0)
ind_max_1 = array2.argmax(axis=1)