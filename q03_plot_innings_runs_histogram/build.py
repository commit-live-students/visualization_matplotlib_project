import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    my_df = ipl_df.groupby(['inning','match_code']).sum()
    fst_inn = my_df.loc[1]['total']
    scn_inn = my_df.loc[2]['total']
    fig, axes = plt.subplots(nrows = 1, ncols = 2)
    axes[0].hist(fst_inn)
    axes[0].set_title('1st Innings')
    axes[1].hist(scn_inn)
    axes[1].set_title('2nd Innings')
    plt.show()
