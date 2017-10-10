import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    grouped = ipl_df.groupby(['batsman','match_code'])
    df_runs = grouped.agg({'runs':'sum'},).reset_index()
    df_balls = grouped.agg({'delivery':'count'},).reset_index()
    x_axis = df_balls['delivery']
    y_axis = df_runs['runs']
    plt.scatter(x_axis,y_axis)
    plt.show()
# Solution
