# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution

def plot_deliveries_by_team():
    x=ipl_df.groupby('batting_team').delivery.count()
    plt.bar(x.index,x.values)
    plt.show()
    
plt.bar([1,2,3],[1,4,9])
plt.show()
x=ipl_df.groupby('batting_team').delivery.count()
type(x)
plt.bar(x,height=2)
plt.show()
x
x[0]
x[1]
x.index
x.values
u=x.index
np.array(u)


