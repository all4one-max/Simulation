## import libaries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

sns.set(color_codes=True) #Set random number for reproducibility
np.random.seed(123) # simulate normal dist (Std normal: loc = 1 and scale = 1)

x = np.random.normal(size=500, loc = 0, scale = 1)

#Plot
fig = plt.figure(figsize=(10,6))
ax = sns.distplot(x, fit = stats.norm, axlabel = "values", 
                  kde_kws={"color": "r", "lw": 3, "label": "KDE"},
                  fit_kws={"color": "black", "lw": 3, "label": "StdNormal"}
                 )
plt.legend(labels=['Kernel Density','Standard Normal Dist'])
plt.title("Standard Normal Distribution")
plt.show(block=False)