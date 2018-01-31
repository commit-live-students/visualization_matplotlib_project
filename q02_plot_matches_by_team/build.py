import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    matches= ipl_df.groupby(by=['batting_team'])['match_code'].nunique()

    team = matches.index.tolist()
    team_length = range(len(team))
    matches_count = matches.tolist()

    plt.bar(team_length, matches_count)
    plt.xticks(team_length, team, rotation=90)
    plt.show()
