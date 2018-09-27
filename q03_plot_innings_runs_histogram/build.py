# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    i=ipl_df.groupby(['match_code','inning']).agg({'runs':'sum'})
    i1=i.groupby('inning').get_group(1)['runs']
    i2=i.groupby('inning').get_group(2)['runs']
    fig=plt.figure()
    plt.subplot(1,2,1)
    plt.hist(i1)
    plt.subplot(1,2,2)
    plt.hist(i2)
    plt.show()
i=ipl_df.groupby(['match_code','inning']).agg({'runs':'sum'})
type(i)
i.iloc[0,0]
i1=i.groupby('inning').get_group(1)['runs']
i1
i2=i.groupby('inning').get_group(2)['runs']
i2


