import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    team_delivery = ipl_df.pivot_table('delivery', aggfunc = np.count_nonzero, index ='batting_team')

    team_delivery.plot(kind = 'bar')
    plt.show()
