import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_deliveries_by_team():
    df=ipl_df[['batting_team','delivery']]
    new_df=df.groupby('batting_team').count()
    sort_df=new_df.sort_values(by='delivery',ascending=False)
    sort_df.plot(kind='bar')
    plt.show()

# Solution
