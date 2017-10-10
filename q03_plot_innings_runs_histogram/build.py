import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    grouped = ipl_df.groupby(['inning','match_code'])
    df = grouped.agg({'runs':'sum'}).reset_index()
    fltr_frst_inning = df['inning']==1
    fltr_scnd_inning = df['inning']==2
    frst_inning = df[fltr_frst_inning]
    x_frst_inning = frst_inning['runs']
    scnd_inning = df[fltr_scnd_inning]
    x_scnd_inning = scnd_inning['runs']
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].hist(x_frst_inning, bins = 13)
    axes[1].hist(x_scnd_inning, bins = 13)
    plt.show()
# Solution
