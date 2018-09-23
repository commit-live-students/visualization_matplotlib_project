# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
ipl_df
def plot_matches_by_team():
    valuereqd=ipl_df.groupby('batting_team')['match_code'].nunique()
    plt.bar(valuereqd.keys(),valuereqd.values)
    plt.xticks(rotation=90)
    plt.show()

plot_matches_by_team()


