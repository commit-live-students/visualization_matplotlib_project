import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    fig, axes = plt.subplots(nrows=1, ncols=2)
    flt_1 = ipl_df["inning"] == 1
    flt_2 = ipl_df["inning"] == 2
    #print ipl_df[flt_1]["inning"]
    data_1 = ipl_df[flt_1].groupby("match_code")["runs"].sum()
    data_2 = ipl_df[flt_2].groupby("match_code")["runs"].sum()
    #print data_1
    axes[0].hist(data_1)
    axes[1].hist(data_2)
    plt.show()
