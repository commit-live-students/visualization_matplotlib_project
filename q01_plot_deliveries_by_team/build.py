# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
data = ipl_df.pivot_table(values='delivery',index=['batting_team'],aggfunc='count')
data.plot(kind='bar')
plt.title('Number of Deliveries Faced by IPL Teams')
plt.xlabel('IPL Teams')
plt.ylabel('Number of Deliveries')
plt.show()
