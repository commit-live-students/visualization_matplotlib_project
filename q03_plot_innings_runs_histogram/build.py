import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution

    innings_runs =  ipl_df.groupby(['inning','batting_team'])['runs'].sum()
    print innings_runs
    print type(innings_runs)
    print innings_runs.index
    plt.figure(figsize=(10,6))
    #plt.plot (by='inning', kind = 'bar', use_index=True, title = "Runs made in Innings")
    plt.subplot(121)
    innings_runs.loc[1,:].plot(kind = 'bar', use_index=True, title = "Runs made in 1st Inning")
    plt.subplot(122)
    innings_runs.loc[2,:].plot(kind = 'bar', use_index=True, title = "Runs made in 2nd Inning")
    plt.show()

#plot_innings_runs_histogram()
