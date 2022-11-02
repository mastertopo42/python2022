import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
t0 = np.array([30.68, 30.67, 30.67, 30.67, 30.68, 30.68, 30.68, 30.68, 30.68, 30.67])
mean1 = t0.mean()
N = len(t0)
sigma_t = np.sqrt(1 / (N - 1) * np.sum((t0 - mean1)**2))
print("t_mean = ", mean1, "; sigma_t = %.3f" % sigma_t)

l = 1
x_pr = 0.2535
m_st = 0.8915
m_pr = 0.0783
m_gr = 0.3136
M = m_gr + m_pr + m_st
print(M)
y = np.array([0.6615, 0.6315, 0.5915, 0.5515, 0.5115, 0.4715, 0.4315, 0.3315, -0.046, -0.066])
N = len(y)
n = np.array([20, 20, 20, 20, 20, 20, 20, 20, 20, 20])
t = np.array([31.62, 31.24, 30.74, 30.27, 29.84, 29.43, 29.08, 28.46, 31.75, 32.33])
x_cm = np.array([0.336, 0.331, 0.32, 0.308, 0.2995, 0.287, 0.279, 0.254, 0.164, 0.16])

T = np.array(t) / n
print(T)

sigma_y = 0.5e-3
sigma_T = sigma_t / t * T
print(sigma_T)


gs =(4*(3.14**2)*(((1/12)+0.2535**2)*0.8915+(0.3136*(y)**2)))/((0.8915+0.3136+0.0783)*((x_cm)*(T)**2))

gm = np.mean(gs)
print(gs)
print("g_mean = %.3f" % gm)

sigma_gm = np.std(gs) / np.sqrt(N)
print("sigma_gm = %.3f" % sigma_gm)

'''plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$T$, с") # подписи к осям
plt.xlabel("$x$, м")
plt.xlim([0, 0.5])
plt.title('Рис.1. График зависимости периода $T$ от положения призмы $a$') # заголовок
plt.grid(True, linestyle="--") # пунктирная сетка
plt.errorbar(x_cm, T, xerr=sigma_y, yerr=sigma_T, fmt=".k", label="Экспериментальные точки") #␣→точки с погрешностями
plt.plot(x_cm, T, "--r", linewidth=1, label="Кусочно линейная интерполяция") # интерполяция
plt.plot([0.00,0.5], [1.53, 1.53], "--b", linewidth=1, label="Минимум") # минимум
plt.legend() # легенда'''


u = T**2 * M * x_cm
v = y**2
print("u = ", u, "\nv = ", v)

plt.plot(v, u, "+")
#plt.savefig('fig.jpg')
#plt.show()

mu = np.mean(u)
mv = np.mean(v)
mv2 = np.mean(v**2)
mu2 = np.mean(u**2)
muv = np.mean(u * v)
k = (muv - mu * mv) / (mv2 - mv**2)
b = mu - k * mv
print("k = ", k, ", b = ", b)

plt.figure(figsize=(8,6), dpi=100)
plt.ylabel("$u=T^2$, $y^2 \cdot м$, M")
plt.xlabel("$v=y^2$, $м^2$")
plt.title('Рис.2. Наилучшая прямая для линеаризованной зависимости $T(a)$')
plt.grid(True, linestyle="--")
plt.axis([0,0.4 ,0,1.3])
x = np.array([0., 1])
plt.plot(x, k * x + b, "-r",linewidth=1, label="Линейная аппроксимация $u = %.2f v + %.2f$" % (k,b))
plt.errorbar(v, u, xerr= sigma_y, yerr=sigma_T, fmt="ok", label="Экспериментальные точки",ms=3)
plt.legend()
plt.savefig('fig2.jpg')
#plt.show()

c = ((1/12)+0.2535**2)*0.8915
g = ((4*(3.14**2))*c)/b
print(g)

N = len(v)
sigma_k = np.sqrt(1/(N-2) * ( (mu2 - mu**2)/(mv2 - mv**2) - k**2 ) )
sigma_b = sigma_k * np.sqrt(mv2)
sigma_g = sigma_k / k * g

print("sigma_k = %.3f, sigma_b = %.3f" % (sigma_k, sigma_b))
print("sigma_g = %.3f" % (sigma_g))

chi2 = np.sum( ((u - (k * v + b)) / sigma_u)**2 )
doF = N -2
print("chi_2 = ", chi2, ", chi_2/doF = ", chi2 / doF)








