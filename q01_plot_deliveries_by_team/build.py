import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
        team_series = pd.Series(ipl_df["delivery"].values,ipl_df["batting_team"])
        d1 = team_series.groupby(team_series.index).agg('count')
        x = np.array(d1.index)
        y = d1.values.astype(int)

        ind = np.arange(len(x))

        plt.bar(ind,y)
        plt.title("total deliveries played by team")
        plt.xlabel("batting teams")
        plt.ylabel("total deliveries played")
        plt.xticks(ind-1,x,rotation=45)
        plt.show()

plot_deliveries_by_team()
