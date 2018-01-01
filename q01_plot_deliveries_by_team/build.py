# %load q01_plot_deliveries_by_team/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():

    df= DataFrame(ipl_df[['batting_team','delivery']].groupby(['batting_team'])['delivery'].count())
    df.columns=['deliveries']
    df.index.name=['batting_team']
    df.plot(kind='bar')
    plt.show()

plot_deliveries_by_team()
