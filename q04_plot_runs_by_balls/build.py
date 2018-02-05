import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    balls = ipl_df.groupby(by=['match_code','batsman'],as_index=0)[['delivery']].count()
    runs = ipl_df.groupby(by=['match_code','batsman'],as_index=0)[['runs']].sum()
    together = pd.merge(balls,runs,on=['match_code','batsman'])
    together.plot.scatter(x='delivery', y='runs')
    plt.show()
