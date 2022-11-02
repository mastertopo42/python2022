import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1
np.random.seed(0)
data = np.random.normal(mu, sigma, 100000)
plt.hist(data, "auto")
plt.show()