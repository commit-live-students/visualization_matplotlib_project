# %load q02_plot_matches_by_team/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

def plot_matches_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    df=DataFrame(ipl_df[['batting_team','match_code']].groupby(['batting_team'])['match_code'].nunique())
    df.plot(kind='bar')
    plt.show()


plot_matches_by_team()
