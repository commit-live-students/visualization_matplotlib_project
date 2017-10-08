import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


#ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
b = ipl_df['batting_team'].value_counts()

#ipl_df.columns
def plot_deliveries_by_team():
    #print(b.values)
    #print(b.index)
    objects = b.index
    #print(type(objects))
    plt.bar(np.arange(len(b)),b.values)
    plt.xticks(np.arange(len(b)),b.index)
    plt.show()
# Solution
#print(plot_deliveries_by_team())
