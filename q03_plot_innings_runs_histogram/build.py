# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    iplGroupBy = ipl_df.groupby(['match_code','inning']).sum()
    fig, ax = plt.subplots(nrows=1, ncols=2)
    
    #return ipl_df.columns.values
    inningInfo = iplGroupBy.loc[:,'total'].reset_index()
    firstInningBool = inningInfo['inning'] == 1
    secondInningBool = inningInfo['inning'] == 2
    data = list()
    data.append(inningInfo[firstInningBool]['total'])
    data.append(inningInfo[secondInningBool]['total'])
    ax = ax.ravel()
    for idx,ax1 in enumerate(ax):
        maxData = data[idx].max()
        print(maxData)
        bins=np.arange(0,maxData,20)
        ax1.hist(data[idx],bins=bins,linewidth=0.2,edgecolor='black')
        
    fig.show()
    #return inningInfo[firstInningBool]['total']
plot_innings_runs_histogram()

