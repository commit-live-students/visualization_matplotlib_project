import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    teams=np.unique(ipl_df['batting_team'])
    ipl_df['count']=1
    deliveries=ipl_df.pivot_table(index='batting_team',aggfunc=np.sum )
    deliveries_count=deliveries['count']

    plt.xlabel('Teams')
    plt.ylabel('Deliveries Played ')
    plt.bar(teams,deliveries_count)
    plt.xticks(teams,rotation='vertical')
    plt.show()
