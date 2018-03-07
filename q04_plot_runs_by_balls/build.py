import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    df1 = DataFrame(ipl_df[['batsman', 'delivery', 'match_code']].groupby(['batsman', 'match_code'])['delivery'].count())
    df2 = DataFrame(ipl_df[['batsman', 'runs', 'match_code']].groupby(['batsman', 'match_code'])['runs'].sum())
    merge_df=[df1, df2]
    final_df=[df1, df2]
    final_df = pd.concat(merge_df, axis=1)
    one_bats = final_df.loc[['A Ashish Reddy'], :]
    one_bats.plot.scatter('delivery', 'runs')
    plt.show()

#print plot_runs_by_balls()
