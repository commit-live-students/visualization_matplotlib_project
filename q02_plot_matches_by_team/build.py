import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    df = ipl_df.loc[:,['match_code','batting_team']]
    gb = df.groupby(['batting_team'])
    gb1 = gb['match_code'].nunique()
    final = gb1.plot(kind = 'bar')
    final.xlabel('batting_team')
    final.ylabel('number of matches')
    plt.show()

#print plot_matches_by_team()
