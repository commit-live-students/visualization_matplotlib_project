# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_matches_by_team():
    list_of_teams = list((ipl_df.groupby('batting_team')['match_code'].unique()).keys())
    unique_values = []
    for i in range(len(list_of_teams)):
        unique_values.append(len(ipl_df.groupby('batting_team')['match_code'].unique()[i]))
    
    plt.bar(np.arange(13),np.array(unique_values))
    plt.xticks(np.arange(13),np.array(list_of_teams),rotation=90)
    plt.show()
plot_matches_by_team()







