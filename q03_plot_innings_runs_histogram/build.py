# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    plots = ipl_df.groupby(['inning'])['runs'].agg(sum).plot.hist()
    plots.set_xlabel('Innings')
    plots.set_ylabel('Runs')
    
    return plots    

ipl_df['inning']


