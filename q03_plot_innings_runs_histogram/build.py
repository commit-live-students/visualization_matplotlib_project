# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    df=ipl_df[['match_code','inning','runs']].groupby(['match_code','inning']).agg(np.sum).reset_index()
    
    first_inning=df[df['inning']==1]['runs']
    second_inning=df[df['inning']==2]['runs']
    
    fig,axes=plt.subplots(nrows=1,ncols=2,squeeze=False)
    axes[0][0].hist(first_inning)
    axes[0][0].set_title('First Innings Runs')
    axes[0][1].hist(second_inning)
    axes[0][1].set_title('Second Innings Runs')
    
plot_innings_runs_histogram()



