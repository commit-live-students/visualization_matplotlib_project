# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    runs = ipl_df.groupby(['match_code','batsman'])['runs'].sum()
    balls = ipl_df.groupby(['match_code','batsman'])['delivery'].count()
    plt.scatter(runs,balls)
    plt.show()
plot_runs_by_balls()    


