import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('/home/darshind/Workspace/code/visualization_matplotlib_project/data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
        grouped_batsman = ipl_df.groupby('batsman')
        batsman_runs = (grouped_batsman.agg({
        'delivery': 'count',
        'runs': 'sum'}))
        batsman_runs.plot.scatter(x='delivery',y='runs')
plot_runs_by_balls()
