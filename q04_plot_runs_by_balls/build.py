# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_runs_by_balls():
    ipl_runs=ipl_df.groupby(['batsman','match_code'],as_index=False).runs.sum()
    ipl_balls=ipl_df.groupby(['batsman','match_code'],as_index=False).runs.count()
    ipl_balls.rename(columns={'runs':'balls'},inplace=True)
    ipl3=pd.concat([ipl_runs, ipl_balls], axis=1, join='inner')
    fig,axs=plt.subplots(1,1)
    axs.scatter(ipl3['balls'],ipl3['runs'])
    plt.show()
    fig
plot_runs_by_balls()
ipl_balls=ipl_df.groupby(['batsman','match_code'],as_index=False).runs.count()
ipl_balls.rename(columns={'runs':'balls'},inplace=True)
ipl3=pd.concat([ipl_runs, ipl_balls], axis=1, join='inner')
fig,axs=plt.subplots(1,1)
axs.scatter(ipl3['balls'],ipl3['runs'])
fig


