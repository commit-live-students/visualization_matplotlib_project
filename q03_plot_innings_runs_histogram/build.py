# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution

first_inning_dataset = ipl_df.loc[ipl_df['inning']==1]
first_inning_dataset = first_inning_dataset.groupby(['match_code'])['total'].sum()
#bins = 
second_inning_dataset = ipl_df.loc[ipl_df['inning']==2]
second_inning_dataset = second_inning_dataset.groupby(['match_code'])['total'].sum()
#print(second_inning_dataset)
match_code_list = ipl_df['match_code'].unique()

colors = ['b','g']
fig, ax1 = plt.subplots()
ax1.hist([first_inning_dataset,second_inning_dataset], bins = 10,color=colors)
#ax1.set_xlim(list(ipl_df['match_code'].unique()))
#ax1.set_ylim(first_inning_dataset.min(), first_inning_dataset.max())
ax1.set_xlabel('Match Code')
ax1.set_ylabel('Score')


