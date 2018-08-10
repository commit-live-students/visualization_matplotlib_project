# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
#def plot_innings_runs_histogram():
df1=ipl_df.loc[ipl_df['inning']==1].groupby(['match_code']).agg(sum)['total']
df2=ipl_df.loc[ipl_df['inning']==2].groupby(['match_code']).agg(sum)['total']

fig, axes = plt.subplots(1, 2)

df1.hist('match_code', bins=100, ax=axes[0])
df2.hist('match_code', bins=100, ax=axes[1])

plt.show



