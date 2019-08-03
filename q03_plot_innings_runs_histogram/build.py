import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    runs_in_each_inning=ipl_df.pivot_table(aggfunc="sum", index=['match_code','inning']
                   , values="total").reset_index()
    runs_in_each_inning= runs_in_each_inning[['inning','total']]
    fig, axes = plt.subplots(nrows=1, ncols=2)
    first_inning_runs= runs_in_each_inning[runs_in_each_inning['inning']==1]['total']
    second_inning_runs= runs_in_each_inning[runs_in_each_inning['inning']==2]['total']
    first_inning_runs.plot.hist(ax=axes[0] )
    second_inning_runs.plot.hist (ax=axes[1])
    plt.show()
