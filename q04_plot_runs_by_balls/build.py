# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
ipl_df.head()
ipl_df1 = ipl_df[['batsman','runs']]
# Solution
def plot_runs_by_balls():
    a = ipl_df1 .groupby('batsman')['runs'].agg(['sum','count'])
    plt.scatter(a['sum'],a['count'])
    plt.show()
    

#plot_runs_by_balls()

