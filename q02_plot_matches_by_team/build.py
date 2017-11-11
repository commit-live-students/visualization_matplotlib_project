# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'data/ipl_dataset.csv'

ipl_df = pd.read_csv(path, index_col=None)

def plot_matches_by_team():
    Y = ipl_df.groupby('batting_team').agg({'match_code': pd.Series.nunique})
    Y.plot.bar()
    plt.show()



# Solution
