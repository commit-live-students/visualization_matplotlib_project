# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    df1 = ipl_df.groupby(['match_code','batsman']).agg({'delivery':'count','runs':'sum'})
    plt.scatter(df1['delivery'],df1['runs'])
    plt.show()

plot_runs_by_balls()
    

