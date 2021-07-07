# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_innings_runs_histogram():
    df=ipl_df.groupby(['match_code','inning'], as_index =False)['runs'].sum()
    fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
# We can set the number of bins with the  kwarg
    axs[0].hist(df['match_code'], bins=10)
    axs[1].hist(df['inning'], bins=10)
    plt.show()
# Solution




