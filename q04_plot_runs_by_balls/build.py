import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    batsmans=ipl_df.groupby(['match_code','batsman'])
    runs_scored = batsmans['runs'].sum()
    balls_faced = batsmans['runs'].count()
    plt.scatter(runs_scored,balls_faced)
    plt.show()
