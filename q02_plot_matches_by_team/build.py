import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    teams_in_each_match =ipl_df.groupby(['match_code','batting_team']).batting_team.nunique()
    teams_in_each_match.groupby(['batting_team']).count().plot.bar()
    plt.show()
