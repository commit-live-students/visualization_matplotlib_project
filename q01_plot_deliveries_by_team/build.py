import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    td_agg = ipl_df.groupby(['batting_team']).sum()
    plt.bar(np.arange(len(td_agg.index)), td_agg['delivery'])
    plt.xticks(np.arange(len(td_agg.index)), td_agg.index, rotation = 45)
    return plt.show()
