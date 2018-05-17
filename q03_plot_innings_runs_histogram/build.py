# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    data=(ipl_df.groupby(['match_code','inning'])['delivery','runs']).agg(['count','sum'])
    #------------------------PLOT for inning 1 ---------------------------------------
    inning1=data.loc(axis=0)[:,[1]]
    
    d1=inning1['delivery']['count'].values
    r1=inning1['runs']['sum'].values
    
    fig,axs=plt.subplots(1,2)
    #axs[0].hist(d1,bins=50)
    axs[0].hist(r1,bins=50)
    
    #------------------------PLOT for inning 2 ---------------------------------------
    inning2=data.loc(axis=0)[:,[2]]
    
    d2=inning2['delivery']['count'].values
    r2=inning2['runs']['sum'].values
    
    
    #axs[1].hist(d1,bins=100)
    axs[1].hist(r1,bins=100)
    plt.show()
    
plot_innings_runs_histogram()

data=(ipl_df.groupby(['match_code','inning'])['delivery','runs']).agg(['count','sum'])
data

