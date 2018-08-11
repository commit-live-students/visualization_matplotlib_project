# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    delivery = list(ipl_df.groupby(['batsman']).delivery.count())
    runs = list(ipl_df.groupby(['batsman']).runs.agg(sum)) 
    %matplotlib inline
    plt.scatter(delivery, runs)

plot_runs_by_balls()

