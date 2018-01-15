# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    pivot = ipl_df.pivot_table(values=['runs'], index=['match_code'], columns='inning', aggfunc='count')
    inning_1 = pivot['runs'][1]
    inning_2 = pivot['runs'][2]
    plt.subplot(1,2,1)
    inning_1.hist()
    plt.subplot(1,2,2)
    inning_2.hist()
    plt.show()
