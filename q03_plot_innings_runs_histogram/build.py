import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.pyplot.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    first_inning = ipl_df[ipl_df['inning'] == 1]
    second_inning = ipl_df[ipl_df['inning'] == 2]
    plt.subplot(1,2,1)
    plt.hist(first_inning.groupby('match_code',as_index=False).sum()['total'])
    plt.subplot(1,2,2)
    plt.hist(second_inning.groupby('match_code',as_index=False).sum()['total'])
    plt.show()
# Solution
