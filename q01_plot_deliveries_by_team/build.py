import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    deliveries = ipl_df['batting_team'].value_counts()
    #print deliveries

    deliveries.plot(kind = 'bar')

    plt.show()

plot_deliveries_by_team()
# Solution
