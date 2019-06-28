# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
a = ipl_df[ipl_df['inning'] == 1]
b = ipl_df[ipl_df['inning'] == 2]

c = a.groupby('match_code').sum()['runs']
d = b.groupby('match_code').sum()['runs']

fig,axes = plt.subplots(1,2)
axes[0].hist(c)
axes[1].hist(d)
plt.show()

    


