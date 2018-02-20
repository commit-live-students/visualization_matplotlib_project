import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    sum_total = ipl_df.groupby(['match_code','inning']).sum().reset_index()
    first = sum_total(sum_total['runs']==1)
    second = sum_total(sum_total['runs']==2)
    fig,axes = plt.subplots(1,2)
    axes[0].hist(first['runs'])
    axes[1].hiist(second['runs'])
    plt.show()
# Solution
