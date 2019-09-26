import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    x_axis = np.arange(len(ipl_df['batting_team']))
    y_axis = ipl_df['delivery']
    plt.bar(x_axis,y_axis)
    plt.show()


plot_deliveries_by_team()
# Solution
