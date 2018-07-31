# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    fig, axes = plt.subplots(nrows=1,ncols=2,squeeze=False)
    filter_ipl = ipl_df.groupby(['match_code','inning']).agg(np.sum)
    first_inn_runs = filter_ipl.iloc[0::2,2]
    second_inn_runs = filter_ipl.iloc[1::2,2]
    index_matchcode = filter_ipl.index.get_level_values('match_code')[::2,]
    axes[0][0].plot(index_matchcode, first_inn_runs) 
    axes[0][0].plot(index_matchcode, second_inn_runs)
    fig.show()


