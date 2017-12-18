import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
# Solution
def plot_deliveries_by_team():
    ipl_df1=ipl_df.pivot_table('batsman',aggfunc=np.size,index='team1')
    ipl_df1.plot(kind='barh')
    plt.show()
    return

#plot_deliveries_by_team()
