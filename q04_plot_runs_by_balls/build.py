import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    x=ipl_df.groupby(['match_code','batsman'])['delivery'].agg('count')
    y=ipl_df.groupby(['match_code','batsman'])['runs'].agg('sum')
    plt.scatter(y,x)
    plt.show()
