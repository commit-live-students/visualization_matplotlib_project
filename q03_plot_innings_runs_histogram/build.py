import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    match_inning_runs = ipl_df.groupby(by=['match_code', 'inning']).sum()[['runs']]
    inning1_df = match_inning_runs.loc[match_inning_runs.index.get_level_values(1) == 1]
    inning2_df = match_inning_runs.loc[match_inning_runs.index.get_level_values(1) == 2]
    inning1_runs, inning2_runs = inning1_df['runs'], inning2_df['runs']
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].hist(inning1_runs, bins=30)
    axes[1].hist(inning2_runs, bins=30)
    plt.show()
