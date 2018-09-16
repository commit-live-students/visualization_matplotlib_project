# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_innings_runs_histogram():
    df1=ipl_df[ipl_df['inning']==1]
    df2=ipl_df[ipl_df['inning']==2]
    
    df11=df1.groupby(['match_code','inning']).sum()
    df22=df2.groupby(['match_code','inning']).sum()
    
    fig,ax =plt.subplots(nrows=1,ncols=2)
    ax[0].hist(df11['runs'])
    ax[1].hist(df22['runs'])
    
    plt.show()
    
    
plot_innings_runs_histogram()





