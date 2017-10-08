import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    ipl_innings = ipl_df[['match_code','inning','runs']]
    ipl_innings_1 = ipl_innings[ipl_innings['inning']==1]
    ipl_innings_2 = ipl_innings[ipl_innings['inning']==2]
    ipl_runs_1 = ipl_innings_1.groupby('match_code')['runs'].sum()
    ipl_runs_2 = ipl_innings_2.groupby('match_code')['runs'].sum()

    plt.subplot(1,2,1)
    plt.hist(ipl_runs_1.values,bins=10)
    plt.xlabel('Runs Scored in a match')
    plt.ylabel('Number of matches')
    plt.title('1st Innings')
    #plt.xticks(range(0,250,50))


    plt.subplot(1,2,2)
    plt.hist(ipl_runs_2.values)
    plt.xlabel('Runs Scored in a match')
    plt.ylabel('Number of matches')
    plt.title('2nd Innings')
    plt.show()
# Solution
