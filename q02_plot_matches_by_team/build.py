import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)


def plot_matches_by_team():
    team_match_counts = ipl_df.groupby(by='batting_team').agg('nunique').match_code
    row_count = team_match_counts.shape[0]
    x_series = np.arange(0, row_count, 1)
    plt.figure(figsize=(20,5))
    plt.bar(x_series, team_match_counts)
    plt.xlabel('Batting Team')
    plt.ylabel('# of matches')
    plt.title('total number of matches played by each team')
    plt.xticks(x_series, team_match_counts.index, rotation=45)
    plt.show()
plot_matches_by_team()
