# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    data = ipl_df.groupby(['batsman'])
    x = data['delivery'].count()
    y = data['runs'].sum()
    plt.scatter(x,y)
    plt.show()
                          

