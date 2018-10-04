# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    inning_wise_runs = ipl_df.groupby(['match_code', 'inning'])['runs'].sum()
    first_inning_runs = inning_wise_runs[:,1]
    second_inning_runs = inning_wise_runs[:,2]
    fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
    
    axs[0].hist(first_inning_runs)
    axs[1].hist(second_inning_runs)
    
    return



