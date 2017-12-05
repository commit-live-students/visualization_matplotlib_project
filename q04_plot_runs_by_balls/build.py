import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    dfx=ipl_df[['match_code','batsman']]
    dfx['balls']=1
    dfx1=dfx.groupby(['match_code','batsman']).count()
    dfy=ipl_df[['match_code','batsman','runs']]
    dfy1=dfy.groupby(['match_code','batsman']).sum()
    x=dfx1['balls'].values
    y=dfy1['runs'].values
    plt.scatter(x,y)
    plt.show()
# Solution
