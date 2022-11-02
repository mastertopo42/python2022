import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)
data = np.random.random(120000).reshape(200, 200, 3)

fig, img = plt.subplots()
img.imshow(data)
plt.show()