import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    df = ipl_df[['match_code', 'batting_team']]
    matches_df = df.groupby('batting_team').agg({'match_code':'nunique'})
    matches_df_plot = matches_df.plot(kind=bar)
    matches_df_plot.xlabel('batting_team')
    matches_df_plot.ylabel('matches played')
    return matches_df

plt.show()

#print plot_matches_by_team()
