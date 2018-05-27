# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    first_innings = ipl_df['inning'] == 1
    second_innings = ipl_df['inning'] == 2

    fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10,6))
    axes[0].hist(ipl_df[first_innings]['runs'])
    axes[0].set_xlabel('Runs')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('1st Innings')

    axes[1].hist(ipl_df[second_innings]['runs'])
    axes[1].set_xlabel('Runs')
    axes[1].set_ylabel('Frequency')
    axes[1].set_title('2nd Innings')

    plt.tight_layout()
    

