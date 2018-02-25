import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    x = ipl_df.groupby(by='batting_team').nunique()
    x['match_code'].plot(kind='bar')
    plt.title("Matches by Team")
    plt.xlabel("batting team")
    plt.ylabel('number of matches')
    plt.show()
