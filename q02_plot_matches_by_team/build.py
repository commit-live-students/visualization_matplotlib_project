import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('/home/darshind/Workspace/code/visualization_matplotlib_project/data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    team_matches = ipl_df.groupby('batting_team').match_code.nunique()
    team_matches.plot.bar()
plot_matches_by_team()
