# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_runs_by_balls():
    df_s=ipl_df.groupby(['match_code','batsman']).sum()
    df_c=ipl_df.groupby(['match_code','batsman']).count()
    plt.scatter(df_c['delivery'],df_s['runs'])
    plt.show()

