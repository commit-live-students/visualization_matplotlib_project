# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    bat=ipl_df.groupby(['batsman','match_code']).agg({'runs':sum,'delivery':'count'})
    plt.scatter(bat.delivery,bat.runs)
    plt.xlabel('balls faced')
    plt.ylabel('runs scored')
    plt.show()
plot_runs_by_balls()

