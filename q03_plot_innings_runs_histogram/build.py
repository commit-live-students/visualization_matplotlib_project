# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution

def plot_innings_runs_histogram():
    #x = ipl_df.where(ipl_df['inning']==1)['runs']
    x1 = ipl_df.where(ipl_df['inning']==1, other = 0)['runs']
    x2 = ipl_df.where(ipl_df['inning']==2, other = 0)['runs']
    #print(x)
    plt.figure()
    plt.subplot(121)
    plt.hist(x1)
    plt.subplot(122)
    plt.hist(x2)

plot_innings_runs_histogram()


