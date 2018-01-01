# %load q03_plot_innings_runs_histogram/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

def plot_innings_runs_histogram():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    df=DataFrame(ipl_df[['batting_team', 'inning','runs']].groupby(['batting_team','inning'])['runs'].sum())
    piv_tab = df.pivot_table(index='batting_team',columns='inning', values='runs')
    piv_tab.plot(kind='bar',stacked=True)
    plt.show()

plot_innings_runs_histogram()
