import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_deliveries_by_team():
    s1 = ipl_df.groupby('batting_team')['delivery'].agg(['count'])
    plt.bar(np.arange(len(s1)),s1.values)
    plt.title(" Total number of deliveries played")
    plt.xlabel("team Members")
    plt.ylabel("Count of deliveries")
    plt.xticks(np.arange(len(s1)),s1.index,rotation =45)
    plt.show()
