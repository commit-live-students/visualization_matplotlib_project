# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_runs_by_balls():
    a = ipl_df[['batsman','delivery']].groupby('batsman').agg('count')
    b = ipl_df[['batsman','runs']].groupby('batsman').agg(sum)
    plt.scatter(a,b)
    plt.show()

# Solution
plot_runs_by_balls



