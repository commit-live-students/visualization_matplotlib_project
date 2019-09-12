import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    runs= ipl_df.pivot_table('runs', aggfunc=np.sum ,index='match_code',columns='inning')
    runs.plot.hist(histtype='bar')
    plt.show()
