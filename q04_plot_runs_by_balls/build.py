# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_runs_by_balls():
    pivot_runs = ipl_df.pivot_table(index='match_code',values=['runs'], aggfunc='sum')
    pivot_delivery = ipl_df.pivot_table(index='match_code',values=['delivery'], aggfunc='count')
    xtick = range(1,270,6)
    ytick = range(10,300,5)
    plt.figure(figsize=[10,10])

    plt.xticks(xtick,rotation=90)
    plt.yticks(ytick)
    plt.scatter(pivot_delivery,pivot_runs)
    plt.show()

# Solution
plot_runs_by_balls()


