import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    y = ipl_df.groupby(['match_code','batting_team','inning'])['runs'].sum().reset_index()

    y1 = y[y['inning'] == 1]['runs']
    x1 = np.arange(len(y1.index))

    y2 = y[y['inning'] == 2]['runs']
    x2 = np.arange(len(y2.index))

    fig, axes = plt.subplots(nrows = 1, ncols = 2)
    fig.tight_layout()
    axes[0].hist(y1)
    axes[0].set_title('Distribution of runs in 1st innings')
    axes[0].set_xlabel('Runs')
    axes[0].set_ylabel('Freq. (No. of matces)')

    axes[1].hist(y2)
    axes[1].set_title('Distribution of runs in 2nd innings')
    axes[1].set_xlabel('Runs')
    axes[1].set_ylabel('Freq. (No. of matches)')


# Solution
