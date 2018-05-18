# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    pass
    data=ipl_df.groupby(['match_code','batsman'])['runs'].agg(['sum','count'])
    count_balls=data['count'].values
    sum_runs=data['sum'].values
    plt.scatter(count_balls,sum_runs,c=(0,0,0),alpha=.2)
    plt.show()


