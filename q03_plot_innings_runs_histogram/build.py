# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    Run_Per_Innining = ipl_df.groupby([ipl_df['match_code'],ipl_df['inning']]).agg('sum')['runs']
    plt.hist(Run_Per_Innining)
    plt.show()



