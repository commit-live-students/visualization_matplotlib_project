# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution

df=ipl_df[['team1','delivery']]
grp=df.groupby('team1')
count=grp.count()
count.plot.bar()
plt.show()



