import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    data = ipl_df[['batsman','delivery','runs']]
    batsman=data.groupby(['batsman'])
    balls=batsman['delivery'].count()
    runs=batsman['runs'].sum()
    plt.scatter(balls,runs)
    plt.show()
