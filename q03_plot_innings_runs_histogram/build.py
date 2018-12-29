# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    inningwise_data = ipl_df.groupby(['inning','match_code']).sum()
    inningwise_data.sort_index(inplace=True)

    match_codes = list(inningwise_data.loc[(1.0),'runs'].index.values)
    first_innings_scores = list(inningwise_data.loc[(1.0),'runs'])
    second_innings_scores = list(inningwise_data.loc[(2.0),'runs'])

    fig,axes = plt.subplots(1,2)
    
    axes[0].hist(first_innings_scores , bins = 5)

    axes[1].hist(second_innings_scores , bins = 5)


