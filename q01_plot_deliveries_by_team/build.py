import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('/home/darshind/Workspace/code/visualization_matplotlib_project/data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    batting_deliveries = ipl_df[['batting_team','delivery']]
    teams_plot = batting_deliveries.groupby('batting_team').count()
    teams_plot.plot.bar()
plot_deliveries_by_team()
