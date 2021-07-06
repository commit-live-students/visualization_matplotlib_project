# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    runs=pd.DataFrame(ipl_df.groupby(['batsman'])['runs'].sum())
    balls=pd.DataFrame(ipl_df.groupby(['batsman'])['match_code'].count())
    runs_balls=runs.join(balls)
    plt.scatter(runs_balls['runs'],runs_balls['match_code'])
    plt.show();





