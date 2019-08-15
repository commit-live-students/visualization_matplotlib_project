import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    ipl_df1 = ipl_df[['batting_team','delivery']]
    runs = ipl_df1.groupby(['batting_team'], as_index = False).count()

    plt.bar(runs.index, runs['delivery'])
    plt.xticks(runs.index, runs['batting_team'], rotation=45)

    plt.show();
