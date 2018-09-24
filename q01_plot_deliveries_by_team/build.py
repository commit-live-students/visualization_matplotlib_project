

# %load q01_plot_deliveries_by_team/build.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    x = ipl_df['batting_team'].unique()
    y = ipl_df.groupby('batting_team')['batting_team'].count()
    x = sorted(ipl_df['batting_team'].unique())
    plt.bar(x,y,0.35)
    plt.xticks(x, rotation=90)
    plt.show()




