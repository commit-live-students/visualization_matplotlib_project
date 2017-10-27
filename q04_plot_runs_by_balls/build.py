import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    deliveries = ipl_df[['batsman','delivery']].groupby(['batsman']).count()
    runs = ipl_df[['batsman', 'runs']].groupby(['batsman']).sum()
    df = pd.concat([deliveries, runs], axis=1)
    df.plot.scatter('delivery', 'runs')
    plt.show()
