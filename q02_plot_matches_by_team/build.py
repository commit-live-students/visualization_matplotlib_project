import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    df1 = DataFrame(ipl_df['batting_team'].unique())
    df = DataFrame(ipl_df[['match_code', 'batting_team']].groupby(['batting_team'])['match_code'].nunique())
    df.plot(kind = 'bar')
    plt.show()

print plot_matches_by_team()
