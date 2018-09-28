# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    count=ipl_df.groupby(ipl_df['batting_team']).agg('count')
    plt.bar(count.index,count['delivery'])
    plt.title('Deliveries/teams')
    plt.xlabel('batting_teams')
    plt.ylabel('Deliveries')
    plt.show()
plot_deliveries_by_team()

