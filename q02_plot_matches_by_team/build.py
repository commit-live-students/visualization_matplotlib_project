import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    d1 = ipl_df["match_code"].groupby(ipl_df["batting_team"]).agg('nunique')
    x = np.array(d1.index.astype("string"))
    y = d1.values.astype('int')

    ind = np.arange(len(x))

    plt.bar(ind,y)
    plt.title("total matches played by team")
    plt.xlabel("teams")
    plt.ylabel("total matches played")
    plt.xticks(ind,x,rotation = 90)
    plt.show()


plot_matches_by_team()
