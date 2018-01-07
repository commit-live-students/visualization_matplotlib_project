import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_deliveries_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    num_of_deliveries = ipl_df.groupby('batting_team')['delivery'].sum()
    num_of_deliveries.plot()
    plt.xticks(rotation=45)
    plt.show()



# Solution
