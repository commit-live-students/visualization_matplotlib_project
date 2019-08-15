import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    ipl_df1 = ipl_df[['match_code','batsman','delivery','runs']]
    aggregator = {'delivery': 'count',
                 'runs': 'sum'}
    chartaxis = ipl_df1.groupby(['match_code','batsman']).agg(aggregator)

    plt.scatter(chartaxis['delivery'], chartaxis['runs'])
    plt.show()
