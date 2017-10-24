import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    match_codes = np.unique(ipl_df['match_code'])
    my_df = ipl_df.groupby(['match_code', 'batsman']).agg({'delivery':'count', 'runs': 'sum'})
    for i in match_codes:
        x_series = my_df.loc[i]['delivery']
        y_series = my_df.loc[i]['runs']
        plt.scatter(x_series, y_series)
        plt.title(str(i))
        plt.xlabel('Deliveries')
        plt.ylabel('Runs')
        plt.show()
