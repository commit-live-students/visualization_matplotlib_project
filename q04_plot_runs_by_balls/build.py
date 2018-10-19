# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    ipl_df1 = ipl_df[['batsman','delivery']].groupby(['batsman']).count()
    ipl_df2 = ipl_df[['batsman','runs']].groupby(['batsman']).sum()
    ipl_data=ipl_df1.join(ipl_df2, how='inner')
    plt.scatter(ipl_df1, ipl_df2)
    plt.show()
    
plot_runs_by_balls()

