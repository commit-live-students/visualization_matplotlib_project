import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_innings_runs_histogram():
    df = DataFrame(ipl_df[['inning', 'runs', 'batting_team']].groupby(['batting_team', 'inning'])['runs'].sum())
    table = df.pivot_table(index='batting_team', columns='inning', values ='runs')
    table1 = table.sort_index()
    table1.plot(kind='bar', stacked = True)
    plt.show()
