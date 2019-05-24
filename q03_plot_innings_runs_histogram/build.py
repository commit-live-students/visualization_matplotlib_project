import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_innings_runs_histogram():
    testhist=ipl_df.pivot_table('runs',aggfunc=sum,columns='inning',index=['match_code'])
    plt.hist(testhist)
# Solution
    plt.show()
