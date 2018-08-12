import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    y = ipl_df.batting_team.value_counts()
    x = np.arange(len(x.index))
    plt.bar(x,y)
    plt.xticks(x,y.index.values,rotation = 90)
    plt.show()
