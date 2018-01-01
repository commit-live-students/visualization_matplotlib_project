import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    x = ipl_df.groupby('batsman')['delivery'].sum()
    y = ipl_df.groupby('batsman')['runs'].sum()
    plt.scatter(x=x, y=y)
    plt.show()
    return None
