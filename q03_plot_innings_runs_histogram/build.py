# %load q03_plot_innings_runs_histogram/build.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    x = ipl_df.groupby(['match_code', 'inning'])['runs'].sum()
    x1 = x[:,1]
    y1 = x[:,2]
    bins = np.linspace(0, 1, 3)

    fig, ax = plt.subplots(1,2)
    ax[0].hist(x1, bins, alpha = 0.5, color = 'r')
    ax[1].hist(y1, bins, alpha = 0.5, color = 'g')
    plt.show()
    




