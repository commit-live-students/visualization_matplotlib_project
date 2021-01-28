# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_innings_runs_histogram():
    x=pd.crosstab(index=ipl_df.match_code,
                columns=ipl_df.inning,
                values=ipl_df.runs,aggfunc=np.sum)

    x.rename(columns={1:'1st',2:'2nd'},inplace=True)
    ax1=plt.subplot2grid((1,2),(0,0),rowspan=1,colspan=1)
    ax1=plt.hist(x['1st'])
    
    ax2=plt.subplot2grid((1,2),(0,1),rowspan=1,colspan=1)
    ax2=plt.hist(x['2nd'][x['2nd'].isnull()==False])    
    plt.show()

plot_innings_runs_histogram()
plot_innings_runs_histogram()



