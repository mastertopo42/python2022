import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1
np.random.seed(100)
data_x = np.random.poisson(100, 10000)
data_y = np.random.poisson(100, 10000)
xed = np.linspace(60, 140, 80)
yed = np.linspace(60, 140, 80)

distrib, xed, yed = np.histogram2d(data_x, data_y, bins=(xed, yed))
fig, axs = plt.subplots(1, 1)

axs.matshow(distrib)
axs.set_xticklabels([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])
axs.set_yticklabels([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])

plt.show()