# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    bating_Team_data = ipl_df[['batting_team','delivery']]
    deliveries_data = bating_Team_data.groupby(['batting_team',]).count()
    print(deliveries_data.head(5))
    print(type(deliveries_data.index))
    print(type(deliveries_data.values))
    #print(deliveries_data.head(5))
    x_axis = [x for x in range(len(deliveries_data.index))]
    plt.xticks(x_axis, deliveries_data.index, rotation=45)

    plt.bar(x_axis, deliveries_data.values)

    plt.show()

#plot_deliveries_by_team()
