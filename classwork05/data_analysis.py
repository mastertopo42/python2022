import matplotlib
from matplotlib import pyplot as plt
import numpy as np

#Порядковый номер студента задаётся ниже

matplotlib.rcParams.update(matplotlib.rcParamsDefault)


def get_numbers(student):
    return student, (student + 4) % 5 + 3, student % 2 * 10 + 12, (student % 5 * 3 + 7) * 3


def fake_data_generator(seed, vmin=0, vmax=10, size=100):
    import numpy as np
    np.random.seed(seed)
    data = np.random.randint(vmin, vmax, size=20)
    mean = data.mean()
    std = data.std()
    noise = np.random.normal(loc=mean, scale=std ** .5, size=size)
    fake_x = np.array([-5 + i * 20 / size for i in range(size)])

    linear = lambda x, k=(.5 - np.random.rand()) * 15, b=np.random.rand() * 10: k * x + b
    linear_data = linear(fake_x)
    fake_y = linear_data + noise
    return fake_x, fake_y


n = 2                         #Здесть можно задать порядковый номер студента
student_number = n
numbers = get_numbers(student_number)
fake_x, fake_y = fake_data_generator((numbers))
#print(fake_x, fake_y)
plt.title('Fake data')
plt.scatter(fake_x, fake_y, label='DATA')
x_error = (fake_x[1] - fake_x[0])/2
y_error = np.array([np.sqrt(np.abs(y)) for y in fake_y])
plt.errorbar(fake_x, fake_y, yerr=y_error, xerr=x_error, fmt='.', color='tab:orange', label='Кресты')
plt.grid()
plt.minorticks_on()
x_mean = sum(fake_x) / len(fake_x)
y_mean = sum(fake_y) / len(fake_y)
plt.vlines(x_mean, fake_y.min(), fake_y.max(), color='b', linestyle=':', label='mean x='+str(x_mean))
plt.hlines(y_mean, fake_x.min(), fake_x.max(), color='r', linestyle=':', label='mean y='+str(float('{:.1f}'.format(y_mean))))
aprox = np.polyfit(fake_x, fake_y, 1)
polinom = np.poly1d(aprox)
fake_y_aprox = polinom(fake_x)
plt.plot(fake_x, fake_y_aprox, color='k', label='fit')
plt.ylabel(r'$\rho, mm^{-3}$')
plt.xlabel(r'$\xi, cm$')
plt.legend(loc='upper right')
#plt.legend(loc='lower right')
plt.scatter(x_mean, y_mean, color='b', s=40, marker='o')
xi_sq = sum([(fake_y[i] - fake_y_aprox[i])**2 / fake_y[i] for i in range(len(fake_x))])
print('хи-квадрат: ', end='')
print(np.abs(xi_sq)**0.5)
plt.show()