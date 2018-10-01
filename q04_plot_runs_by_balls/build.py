# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

m=ipl_df.groupby('match_code')['bowler'].nunique()
n=ipl_df.groupby('match_code')['bowler','runs'].agg({'runs':'sum'})
plt.scatter(m,n)

plt.show()

# Solution
#def plot_runs_by_balls():#h=ipl_df['bowler'].value_counts.agg('sum')








