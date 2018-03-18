import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_innings_runs_histogram():
    pd_df1 = ipl_df.pivot_table(columns ="inning",values = "runs", index="match_code", aggfunc="sum")
    plt.subplot(121)
    pd_df1[1].plot(kind="hist")
    plt.subplot(122)
    pd_df1[2].plot(kind="hist")
    plt.show()
