import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    delivery_counts =  ipl_df.groupby(['batting_team'])['delivery'].count()
    delivery_counts.plot(kind = 'bar', use_index=True, title = "Deliveries handled by teams", legend = True)
#plot_deliveries_by_team()
