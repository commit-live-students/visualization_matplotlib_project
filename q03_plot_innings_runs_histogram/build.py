# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    df= DataFrame(ipl_df[['batting_team','inning','runs']].groupby(['batting_team','inning'])['runs'].sum())
    piv_tab = df.pivot_table(index='batting_team',columns='inning', values='runs')
    piv_tab.plot(kind='bar',stacked=True)
    plt.show()
    return plt.show()
print plot_innings_runs_histogram()
