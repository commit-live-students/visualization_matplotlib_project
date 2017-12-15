import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_matches_by_team():
    counter=ipl_df.groupby("batting_team").agg({"match_code": pd.Series.nunique})
    counter.plot(kind='bar')
    plt.show()
