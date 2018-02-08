import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    no_of_delivery_faced= ipl_df.pivot_table('delivery',aggfunc ='count', index='batting_team')
    no_of_delivery_faced.plot(kind ='bar')
    plt.show()
