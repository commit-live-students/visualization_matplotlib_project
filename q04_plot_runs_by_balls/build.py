import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    pd_df1 = ipl_df.pivot_table(index="delivery",values="runs", columns=["match_code"], aggfunc="count")
    balls_played = ipl_df.groupby(["match_code","inning","batsman"])["delivery"].count()
    runs_scored =  ipl_df.groupby(["match_code","inning","batsman"])["runs"].sum()
    plt.scatter(runs_scored,balls_played)
    plt.show()
