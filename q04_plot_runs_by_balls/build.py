import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    bats_run_df=ipl_df[['batsman','runs','delivery']]
    hh=ipl_df.groupby('batsman').agg({ 'runs': {'sum': 'sum', 'count': 'count'}})
    hhh=hh['runs']
    hhh.plot(kind='scatter',x='count',y='sum')
    plt.show()
