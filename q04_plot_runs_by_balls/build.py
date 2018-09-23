# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
# def plot_runs_by_balls():
df = ipl_df[['match_code','batsman','delivery', 'runs']].groupby(['match_code','batsman']).agg({'delivery':'count', 'runs':'sum'}).reset_index()
df
# plt.scatter(df['delivery'], df['runs'])
# plt.show()


