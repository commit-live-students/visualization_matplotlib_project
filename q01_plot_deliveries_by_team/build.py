import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    ipl_df[['batting_team','runs']].groupby('batting_team').count().plot(kind='bar')
    plt.show()

#plot_deliveries_by_team()
