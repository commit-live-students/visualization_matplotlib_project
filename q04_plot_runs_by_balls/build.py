# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    runs_per_delivery=ipl_df[['runs','delivery']].groupby('delivery').sum()
    plt.scatter(runs_per_delivery.index,runs_per_delivery['runs'])
    plt.show()



