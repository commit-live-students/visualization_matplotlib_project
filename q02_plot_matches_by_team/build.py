import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    delivery_counts =  ipl_df.groupby(['batting_team'])['match_code'].nunique()
    print delivery_counts
    delivery_counts.plot(kind = 'bar', use_index=True, title = "Matches played by teams")
    plt.show()

#plot_matches_by_team()
