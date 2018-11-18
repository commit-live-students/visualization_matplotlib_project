# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    teams= ipl_df.groupby('batting_team').count()
    series= teams['delivery']
    plt.xlabel('Batting Team')
    plt.ylabel('Deliveries')
    plt.title('Deliveries by Team')
    plt.bar(series.index,series)
    plt.show()
plot_deliveries_by_team()







