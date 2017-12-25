import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    ipl_df1 = ipl_df[['batting_team','match_code']]


    aggregation = {'match_code': 'nunique'}
    uniquecount = ipl_df1.groupby('batting_team').agg(aggregation).reset_index()

    # print uniquecount
    plt.bar(uniquecount.index, uniquecount['match_code'])
    plt.xticks(uniquecount.index, uniquecount['batting_team'], rotation=90)
    plt.show()
