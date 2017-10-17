# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    df1 = ipl_df.groupby(['match_code','batsman'])['runs'].sum().reset_index()
    df2 = ipl_df.groupby(['match_code','batsman'])['delivery'].count().reset_index()
    df3 = pd.merge(df1,df2,how='outer', on=['match_code','batsman'])
    plt.scatter(df3['delivery'],df3['runs'])
    plt.show()
    return
