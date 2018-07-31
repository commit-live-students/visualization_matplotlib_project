# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_deliveries_by_team():
    bar_plot = ipl_df.groupby(['team1'])['delivery'].count().plot.bar()
    bar_plot.set_xlabel('teams')
    bar_plot.set_ylabel('counts of deliveries')

#    batting_team = ipl_df['batting_team']
#    deliveried_face_by_team = batting_team.value_counts()

#    x_axis = np.arange(len(deliveried_face_by_team.index))
#    plt.bar(x_axis, deliveried_face_by_team)
#    plt.xticks(x_axis, deliveried_face_by_team.index.values)
#    plt.show()
    
    return

plot_deliveries_by_team()


