import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_runs_by_balls():
    run_scored=ipl_df.groupby('batsman').runs.sum()
    ball_played=ipl_df['batsman'].value_counts()
    data_merge=pd.concat([run_scored,ball_played],axis=1)
    plt.scatter(x= data_merge['runs'],y=data_merge['batsman'])
    plt.show()

plot_runs_by_balls()
