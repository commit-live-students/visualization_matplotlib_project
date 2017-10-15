import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    data = ipl_df['batting_team']
    xy = data.groupby(ipl_df['batting_team']).count().sort_values(ascending=False)
    x_label = range(1,14)
    y_label = xy
    plt.bar(x_label,y_label)
    plt.xticks(x_label, xy.index, rotation=90)
    plt.show()
    return
plot_deliveries_by_team()
