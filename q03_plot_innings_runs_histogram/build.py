# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    per_match_runs = ipl_df[['match_code', 'inning']].groupby('inning').agg('sum')     
    plt.hist(per_match_runs)
    plt.show()
    print(per_match_runs)
    
plot_innings_runs_histogram()



