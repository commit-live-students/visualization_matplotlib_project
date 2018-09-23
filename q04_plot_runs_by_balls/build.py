# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    df=ipl_df[['inning','runs']]
    df1=pd.DataFrame(ipl_df['inning'].value_counts())
    df2=pd.DataFrame(ipl_df.groupby(['inning'])['runs'].sum())
    runs_vs_balls=df1.join(df2)
    plt.scatter(runs_vs_balls['inning'],runs_vs_balls['runs'])
    plt.show()





