# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

#Function create
def plot_innings_runs_histogram():
    '''Function to plot and analyze teams performance in 1st Innings vs 2nd Innings'''
    #dataframe subsetting for one team and each innings
    ipl_df_1 = ipl_df[(ipl_df['batting_team']=='Kolkata Knight Riders') & (ipl_df['inning']==1)]
    ipl_df_2 = ipl_df[(ipl_df['batting_team']=='Kolkata Knight Riders') & (ipl_df['inning']==2)]

    #Series of runs for each innings to plot
    innings1 = ipl_df_1.groupby(['match_code']).sum()['runs']
    innings2 = ipl_df_2.groupby(['match_code']).sum()['runs']

    #Subplots with two columns and plotting each innings
    fig,axs = plt.subplots(ncols=2,nrows=1)
    axs[0].hist(innings1, label = '1st innings')
    axs[1].hist(innings2, label = '2nd innings')
    axs[0].legend()
    axs[1].legend()
    fig.tight_layout() #align the loyout to avoid overlapping
    plt.show()

#Function call
plot_innings_runs_histogram()
#plot_innings_runs_histogram()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram()
    ipl_df_1 = ipl_df[(ipl_df['batting_team']=='Kolkata Knight Riders') & (ipl_df['inning']==1)]
    ipl_df_2 = ipl_df[(ipl_df['batting_team']=='Kolkata Knight Riders') & (ipl_df['inning']==2)]

    innings1 = ipl_df_1.groupby(['match_code']).sum()['runs']
    innings2 = ipl_df_2.groupby(['match_code']).sum()['runs']


    fig,axs = plt.subplots(ncols=2,nrows=1)
    axs[0].hist(innings1, label = '1st innings')
    axs[1].hist(innings2, label = '2nd innings')
    axs[0].legend()
    axs[1].legend()
    fig.tight_layout()
    plt.show()


plot_innings_runs_histogram()



