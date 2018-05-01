# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
ipl_df.head()
def plot_innings_runs_histogram():
    pivot_data = ipl_df.pivot_table(columns='inning',index=['match_code'],values='runs',aggfunc='sum')
    inning_1 = pivot_data[1].astype(np.int)
    x_1 = list(inning_1)
    inning_2 = pivot_data[2]
    nanfinder = np.isnan(inning_2.values)
    inning_2[nanfinder]=0
    x_2 = list(inning_2.astype(np.int))
    # Solution
    fig, axes = plt.subplots(nrows=1,ncols=2,figsize=[10,5])
    axes[0].hist(x_1,bins=50,color='red')
    axes[1].hist(x_2,bins=50)
    plt.tight_layout()
    plt.show()

plot_innings_runs_histogram()


