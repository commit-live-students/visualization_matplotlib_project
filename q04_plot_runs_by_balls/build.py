# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    runs= ipl_df.groupby(['batsman','match_code'], as_index=False)['runs'].sum()
    ball = ipl_df.groupby(['batsman','match_code'], as_index=False)['delivery'].count()
    result = pd.concat([runs, ball], axis=1, join='inner')
    plt.scatter(result['delivery'],result['runs'])
    plt.show()
# Solution




