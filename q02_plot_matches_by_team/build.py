# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_teams():
    a=ipl_df.groupby('batting_team').match_code.nunique()
    plt.bar(a.index, a.values)
    plt.show()
    a=ipl_df.groupby('batting_team').match_code.nunique()
    a.index
    a.values
    plt.bar(a.index,a.values)
    plt.show()



