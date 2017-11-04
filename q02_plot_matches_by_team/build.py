import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.pyplot.switch_backend('agg')

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    batting_teams_data = ipl_df.groupby(['batting_team','match_code'],as_index=False).count()[['batting_team','match_code']]
    team_data = batting_teams_data['batting_team'].value_counts()
    team_data.plot(kind='bar')
    plt.show()
