def task1():
    # TODO: первое задание
x = int(input())
x = x^2
print(x)

def task2():
    # TODO: второе задание
a = input().split()
nums = [int(num) for num in filter(lambda  num: num.isnumeric(), a)]
print(nums)

def task3():
    # TODO: третье задание

def task4(generator):
    # TODO: четвертое задание
a = [x for x in range(-10, 11)]
b = list(filter(lambda x:  (x % 2 == 0), a))
print(*b)

def task5(list_of_smth):
    # TODO: пятое задание
s = input()
n = len(s)
s1 = s[4:n-1:5]
print(s1) 

def task6(list1, list2, list3, list4):
    # TODO: шестое задание
def joiner (a,b)
    a = list(input().split())
    b = list(input().split())
    c = []
     for i in a:
        for j in b:
            if i == j:
                c.append(i)
                break
    return c

g = joiner(m,n)
f = joiner(l,p)

def task7():
    # TODO: седьмое задание
import numpy as np
matrix = np.random.randint(36, size=(6,6))
print(matrix)
print(matrix[:5:1,1::1])
print(np.linalg.det(matrix[:5:1,1::1]))


def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: восьмое задание
import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x*x*x

x_min = -10
x_max = 10
N = 10
y_min = -1000
y_max = 1000

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.linspace(x_min, x_max, N)
plt.scatter(x, f(x))
plt.ylim((y_min, y_max))
plt.grid(True)
x = np.linspace(x_min, x_max, 1000000)
plt.plot(x, f(x), color = "red")
plt.savefig("function.jpeg")
    

def task9(data, x_array, y_array):
    # TODO: ...

def task10(list_of_smth):
    # TODO: ...

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    # TODO: ...
