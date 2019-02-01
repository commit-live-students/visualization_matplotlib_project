# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    i=ipl_df.groupby(['match_code','inning']).agg({'runs':'sum'})
    t1=i.groupby('inning').get_group(1)['runs']
    t2=i.groupby('inning').get_group(2)['runs']
    fig=plt.figure()
    plt.subplot(1,2,1)
    plt.hist(t1)
    plt.subplot(1,2,2)
    plt.hist(t2)
    plt.show()
    i=ipl_df.groupby(['match_code','inning']).agg({'runs':'sum'})
    type(i)
    i.iloc[0,0]
    t1=i.groupby('inning').get_group(1)['runs']
    t1
    t2=i.groupby('inning').get_group(2)['runs']
    2


