# %load q04_plot_runs_by_balls/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

def plot_runs_by_balls():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    df1 = DataFrame(ipl_df[['batsman','delivery','match_code']].groupby(['batsman','match_code'])['delivery'].count())
    df2 = DataFrame(ipl_df[['batsman','runs','match_code']].groupby(['batsman','match_code'])['runs'].sum())
    merg_df=[df1,df2]
    final_df = pd.concat(merg_df,axis=1)
    one_bats = final_df.loc[['A Ashish Reddy'],:]
    one_bats.plot.scatter('delivery','runs')
    plt.show()

plot_runs_by_balls()
