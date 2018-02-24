import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    #print ipl_df.unique(['batting_team', 'match_code'])
    df = ipl_df.groupby('batting_team')
    matches_by_team = df['match_code'].nunique()
    #print matches_by_team
    matches_by_team.plot(kind='bar')
    plt.show()

plot_matches_by_team()
