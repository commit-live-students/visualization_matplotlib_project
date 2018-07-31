# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_matches_by_team():
    filter_team = ipl_df.groupby(['batting_team']).agg('nunique')
    xseries = filter_team.index
    yseries = filter_team['match_code']
    plt.plot(xseries,yseries)
    plt.show()
    

