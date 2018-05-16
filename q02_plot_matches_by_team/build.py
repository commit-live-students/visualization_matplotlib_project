# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    
    a=ipl_df.groupby('batting_team')['match_code'].agg('unique')
    b=a.index.values
    c=[]
    for arr in a:
        c.append(len(arr))
    plt.bar(b,c)
    plt.xticks(rotation=45)
    plt.show()


