import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    runs_scored = ipl_df.groupby(['match_code','inning']).agg({'runs' : sum}).reset_index()

    runs1 = np.array(runs_scored[runs_scored['inning']==1])
    plt.subplot(1,2,1)
    plt.xlabel('Runs')
    plt.ylabel('Occurence')
    plt.title('1st Innings')
    plt.hist(runs1[:,2])

    runs2 = np.array(runs_scored[runs_scored['inning']==2])
    plt.subplot(1,2,2)
    plt.xlabel('Runs')
    plt.ylabel('Occurence')
    plt.title('2nd Innings')
    plt.hist(runs2[:,2])

    plt.show()
