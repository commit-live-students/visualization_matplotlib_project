import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    fig,(ax1,ax2) = plt.subplots(1,2)
    innings1 = ipl_df[ipl_df["inning"]==1]
    a1 = innings1["runs"].groupby(innings1["batting_team"]).sum()
    innings2 = ipl_df[ipl_df["inning"]==2]
    a2 = innings2["runs"].groupby(innings2["batting_team"]).sum()

    ax1.hist(a1.values)
    ax2.hist(a2.values)




plot_innings_runs_histogram()
