# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    a=ipl_df.groupby('batting_team').count()
    b=a['delivery']
    plt.bar(a.index,b)
    plt.xticks(rotation=90)
    plt.show()

    print(plot_deliveries_by_team())

plot_deliveries_by_team()

