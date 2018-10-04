# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    i1=ipl_df[ipl_df['inning']==1]
    x=i1.groupby(ipl_df['match_code']).agg('sum')

    i2=ipl_df[ipl_df['inning']==2]
    y=i2.groupby(ipl_df['match_code']).agg('sum')
    fig, axs = plt.subplots(1, 2, sharey=True)
    axs[0].hist(x['runs'])
    axs[1].hist(y['runs'])
    fig.show()
plot_innings_runs_histogram()

