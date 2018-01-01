# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    df1= DataFrame(ipl_df[['batsman','delivery','runs']].groupby(['batsman'])['delivery'].count())
    df2= DataFrame(ipl_df[['batsman','delivery','runs']].groupby(['batsman'])['runs'].sum())
    result = pd.concat([df1, df2], axis=1)
    result.plot.scatter('delivery','runs')
    plt.show()
    return plt.show()
