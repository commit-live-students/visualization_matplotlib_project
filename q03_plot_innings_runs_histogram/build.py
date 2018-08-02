# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_innings_runs_histogram():
    a =ipl_df[ipl_df['inning'] == 1][['match_code','runs']].groupby('match_code').agg(sum)
    b =ipl_df[ipl_df['inning'] == 2][['match_code','runs']].groupby('match_code').agg(sum)
    plt.figure(1)
    plt.subplot(211)
    plt.hist(a)
    plt.show()
    plt.subplot(212)
    plt.hist(b)
    plt.show()
# Solution
plot_innings_runs_histogram()



