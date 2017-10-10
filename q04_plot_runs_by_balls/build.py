import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    R = ipl_df.groupby(["match_code","batsman"])["runs"].sum()
    B = ipl_df.groupby(["match_code","batsman"])["delivery"].count()
    RB = pd.concat([R,B], axis=1, join_axes=[R.index])
    #print RB
    plt.scatter(RB["delivery"],RB["runs"], c="b")
    plt.show()
