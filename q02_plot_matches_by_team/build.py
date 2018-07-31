# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    plots = ipl_df.groupby(['team1'])['match_code'].nunique().plot.bar()
    plots.set_xlabel('Team')
    plots.set_ylabel('Matches Played')
    
    return plots

plot_matches_by_team()




