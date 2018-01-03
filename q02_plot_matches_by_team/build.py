import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_matches_by_team():
    umatches = ipl_df[['batting_team','match_code']].groupby('batting_team').agg({'match_code':pd.Series.nunique})
    umatches.plot(kind='bar')
    #plt.show()
    return None
