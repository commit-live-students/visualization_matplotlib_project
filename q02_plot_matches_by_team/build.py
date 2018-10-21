# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    x_team = ipl_df['batting_team']
    #y_count = ipl_df.groupby('batting_team')['match_code'].count()
    y_count = ipl_df['match_code']
    #print(y_count)
    plt.scatter(x_team,y_count)
    plt.plot(x_team,y_count)
    plt.show()
# Solution
plot_matches_by_team()



