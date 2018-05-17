# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution

def plot_runs_by_balls():
    runs=ipl_df.groupby(['batsman']).agg({'runs':'sum'})
    balls=ipl_df.groupby(['batsman']).agg({'delivery':'count'})
    #plt.figure(figsize=(25,25))
    plt.scatter(runs,balls)
    plt.show()
    
#plot_runs_by_balls()


