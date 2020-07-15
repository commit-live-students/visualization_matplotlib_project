# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')


ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_innings_runs_histogram():
    plt.subplot(1,2,1)
    plt.hist(innings_1_runs,rwidth=0.9)
    plt.legend(['First Innings'])

    plt.subplot(1,2,2)
    plt.hist(innings_2_runs,rwidth=0.9)
    plt.legend(['Second Innings'])

    plt.show()





