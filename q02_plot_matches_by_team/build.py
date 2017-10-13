# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

#print(ipl_df.head(5))

# Solution
def plot_matches_by_team():
    bating_Team_data = ipl_df[['batting_team','match_code']]
    deliveries_data = bating_Team_data.groupby(['batting_team',]).agg('nunique')
    print(deliveries_data.head(5))

    #print(type(deliveries_data.index))

    #print(type(deliveries_data.values))
    #print(deliveries_data.head(5))
    x_axis = [x for x in range( len(deliveries_data.index))]
    print(x_axis)
    print(len(deliveries_data.index))
    #print(len(deliveries_data['match_code']))



    plt.bar(x_axis, deliveries_data['match_code'])
    plt.xticks(x_axis, deliveries_data.index, rotation=90)
    plt.show()
    print(deliveries_data.index[12])

#plot_matches_by_team()
