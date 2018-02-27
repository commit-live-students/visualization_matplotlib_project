import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_innings_runs_histogram():

    s = ipl_df.groupby(['inning','total'])
    print s['total'].sum()
    #plt.hist()

plot_innings_runs_histogram()
