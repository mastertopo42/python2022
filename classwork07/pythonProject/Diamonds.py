import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print(diamonds)

#print(diamonds[(diamonds['x'] > 5) & (diamonds['y'] > 5) & (diamonds['z'] > 5)])

dm = diamonds.select_dtypes(include=('int', 'float'))
#print(dm)

#print(dm.mean())

#print(diamonds.groupby(["cut"]).agg({"price": "mean"}))
#f = diamonds.groupby(["cut"]).agg({"price": "mean"})
#f.plot()
#plt.show()

#g = diamonds.groupby(["cut"])
#g.plot()
plt.hist(diamonds['cut'],'auto')
plt.show()
