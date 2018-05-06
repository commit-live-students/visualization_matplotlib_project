# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
#list(ipl_df)
ipl_res_df = ipl_df.groupby(['batting_team'])['delivery'].count()
ipl_del_count_list = ipl_res_df.tolist()
ipl_del_team_list = list(ipl_res_df.index.values)
plt.bar(ipl_del_team_list,ipl_del_count_list)
plt.xticks(ipl_del_team_list,rotation=45)
plt.show()
#ipl_df['batting_team'].unique()




