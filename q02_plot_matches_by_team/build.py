import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_matches_by_team():

    # Calculate the unnique of match_code column by batting_team
    batting_team = ipl_df['match_code'].groupby(ipl_df['batting_team']).agg('nunique')
    batting_team.plot(kind = 'bar')
    plt.show()
