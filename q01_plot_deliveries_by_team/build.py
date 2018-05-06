# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_deliveries_by_team():
    ser = ipl_df.groupby(['batting_team']).count()['match_code']
    y_pos = np.arange(len(ser))
    plt.bar(y_pos, ser, align='center', alpha=0.5)
    x_pos = ser.index
    plt.xticks(y_pos, x_pos, rotation=90)
    plt.ylabel('Deliveries')
    plt.title('Teams Vs Deliveries')
    plt.show()






