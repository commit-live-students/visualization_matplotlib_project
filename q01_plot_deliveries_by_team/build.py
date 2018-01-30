import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    y = ipl_df.groupby(['batting_team'])['delivery'].count()
    x = np.arange(len(y.index))

    plt.bar(x,y)
    plt.xticks(x,y.index,rotation=90)
    plt.xlabel('Teams')
    plt.ylabel('No. of deliveries')
    plt.title('No. of deliveries played by each team')
    plt.show()
    
# Solution
