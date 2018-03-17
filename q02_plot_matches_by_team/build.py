import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    pd_df = ipl_df.groupby("batting_team")["match_code"].nunique()
    pd_df.plot(kind="bar")
    plt.show()
