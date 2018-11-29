#%load q04_plot_runs_by_balls/build.py

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

ifl_df=pd.read_csv('./data/ipl_dataset.csv')
# ifl_df.columns
# runs,delivery,batsman

def plot_runs_by_balls():

    gr=ifl_df.groupby('batsman')
    balls=pd.DataFrame(gr['delivery'].count())
    runs=pd.DataFrame(gr['runs'].sum())

    A=balls.merge(runs, left_index=True,right_index=True, how='inner')

    plt.scatter(A.runs,A.delivery)
    plt.xlabel=('runs')
    plt.ylabel=('deliveries')

    plt.show()

# runs

# plt.scatter(ifl_df[)


