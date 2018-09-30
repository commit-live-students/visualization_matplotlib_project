# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

plt.figure()
#def plot_innings_runs_histogram()
df1=ipl_df.loc[ipl_df['inning'] == 1]
df2=ipl_df.loc[ipl_df['inning'] == 2]
value1=df1['runs']
value2=df2['runs']

bins1=df1['match_code'].nunique()
bins2=df2['match_code'].nunique()


plt.subplot(1,2,1)
plt.hist(value1,bins1)

plt.subplot(1,2,2)
plt.hist(value2,bins2)

plt.show()

