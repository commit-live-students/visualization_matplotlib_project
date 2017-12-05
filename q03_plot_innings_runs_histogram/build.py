import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    data=ipl_df[['batting_team','inning','runs']]
    g_inning=data.groupby(['batting_team','inning'])
    runs=g_inning['runs'].count().unstack()
    plt.subplot(1,2,1)
    plt.hist(runs[1])
    plt.subplot(1,2,2)
    plt.hist(runs[2])
    plt.show()
