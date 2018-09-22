# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_matches_by_team():
    nunique_matches=ipl_df.groupby(['team1'])['match_code'].nunique()
    nunique_matches.plot(kind='bar')
    plt.show();
plot_matches_by_team()



