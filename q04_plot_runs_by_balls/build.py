# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_runs_by_balls():
    run_details = ipl_df.groupby(['match_code', 'batsman']).agg({'runs': ['count', 'sum']})['runs']
    plt.scatter(run_details['count'], run_details['sum'])
    plt.show()

plot_runs_by_balls()

