import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    df=ipl_df[['batting_team','delivery']]
    counts=df.groupby('batting_team').count()
    sort=counts.sort_values(by='delivery',ascending=False)
    sort.plot(kind='bar')
    plt.show()
