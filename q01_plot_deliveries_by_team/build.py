import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    df = ipl_df[['delivery', 'batting_team']]
    df['count'] = 1
    deliveries_by_team = df.pivot_table('count', aggfunc=np.sum, index='batting_team')
    deliveries_by_team_plot = deliveries_by_team.plot(kind='bar')
    deliveries_by_team_plot.xlabel('batting_team')
    deliveries_by_team_plot.ylabel('delivery')
    return deliveries_by_team_plot

plt.show()




#print plot_deliveries_by_team()
