import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    y = ipl_df[['batting_team','match_code']].groupby(['batting_team']).agg('nunique')
    x = np.arange(len(y.index))
    plt.bar(x,y1['match_code'])
    plt.xlable('Team Names')
    plt.ylable('Matches Played')
    plt.xticks(x,y.index.values,rotation = 90)
    plt.show()
