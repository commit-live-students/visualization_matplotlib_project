# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    d = ipl_df.groupby(['match_code','batsman'])['runs','delivery'].agg({'delivery':'count', 'runs':'sum' })
    plt.figure(figsize=(20,20))
    plt.scatter(d.delivery, d.runs)
    plt.show()
plot_runs_by_balls()


