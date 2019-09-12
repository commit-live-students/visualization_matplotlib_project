import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_runs_by_balls():
    runs= ipl_df.pivot_table('runs', aggfunc=np.sum ,index='match_code')
    balls= ipl_df.pivot_table('delivery', aggfunc='count',index='match_code')
    runs = pd.merge(runs,balls,left_index=True,right_index=True)
    runs.plot(kind='scatter', x='delivery',y='runs')
    plt.show()
