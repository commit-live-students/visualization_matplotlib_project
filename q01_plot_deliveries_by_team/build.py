import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    a = ipl_df[['batting_team','delivery']]
    b = pd.groupby(a,by = 'batting_team').count()
    b.plot(kind='bar')
    plt.show()



# Solution
