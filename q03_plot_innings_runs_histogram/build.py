import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    #runs per match
    count_runs = ipl_df[['inning','match_code','runs']]
    pivot_count_runs=count_runs.pivot_table('runs',aggfunc=np.sum,index='match_code',columns='inning').fillna(0)
    left=pivot_count_runs

    #Count of bowls played per bowler
    ipl_df['frequency']=1
    count_balls=ipl_df[['inning','bowler','frequency']]
    pivot_count_balls=count_balls.pivot_table('frequency',aggfunc=np.sum,index='bowler',columns='inning').fillna(0)
    right=pivot_count_balls

    #Merging two dataframes to get runs per inning
    merge_df=pd.merge(left,right,how='outer')
    print merge_df.head()

    plt.hist(merge_df,bins=250)
    plt.subplots(1,2)
    xaxes=['1','2']
    yaxes=['runs']
    plt.title('Runs per innings')
    plt.xlabel('Matches')
    plt.ylabel('Runs Scored')

    plt.show()
plot_innings_runs_histogram()
