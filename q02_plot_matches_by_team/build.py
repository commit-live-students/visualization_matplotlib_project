import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    ipl_df['count'] = 1
    data = ipl_df[['batting_team','match_code','count']]
    matches = data.groupby(['batting_team','match_code']).agg(np.unique)
    teams = matches['count'].groupby(['batting_team']).sum()
    bar_plot = teams.plot(kind = 'bar')
    plt.show()
