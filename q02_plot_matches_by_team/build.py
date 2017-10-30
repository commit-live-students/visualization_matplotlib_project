import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    x = ipl_df.groupby(['batting_team','match_code']).agg('nunique')
    index = x.index
    i = range(0,len(index))
    y = x['match_code']
    plt.bar(i, y.values)
    plt.xticks(i,index,rotation=90)
    plt.show()
# Solution
