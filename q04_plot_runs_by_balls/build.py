# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    df=ipl_df[['inning','runs']]
    df1=ipl_df['inning'].value_counts()
    df2=df.groupby('inning')['inning'].sum()
    x=df1.tolist()
    y=df2.tolist()
    plt.scatter(x, y,alpha=0.5)
    plt.show()





