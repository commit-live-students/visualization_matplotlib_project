# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_matches_by_team():
    a=ipl_df.groupby(by='batting_team').nunique()
    plot=a['match_code'].plot(kind='bar')
    plot.set_ylabel("Match_Count")
    plot.set_xlabel("Teams")
    plt.show()
plot_deliveries_by_team()
