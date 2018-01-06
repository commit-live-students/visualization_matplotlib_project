import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_deliveries_by_team():
    #ipl_df['count'] = 1
    bardt = ipl_df.pivot_table('delivery', aggfunc = np.size, index ='batting_team')
    plt.title('deliveries_by_team')
    plt.xlabel('batting team')
    plt.ylabel('no of deliveries')
    bardt.plot(kind = 'bar')
    plt.show()

# Solution
