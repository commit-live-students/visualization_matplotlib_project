import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('/home/darshind/Workspace/code/visualization_matplotlib_project/data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():

    grouped = ipl_df.groupby('inning')
    grouped_plot = (grouped.agg({
    'delivery': 'count',
    'total': 'sum'}))
    grouped_plot.plot.bar()
plot_innings_runs_histogram()
