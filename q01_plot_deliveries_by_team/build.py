# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution

df=ipl_df
df=pd.DataFrame(df)
s=df.groupby('delivery').agg(pd.Series.nunique)
r=df.groupby('batting_team').agg(pd.Series.nunique)
a=list(r['delivery'].index)
b=list(r['delivery'])
plt.bar(a,b)
#plt.show()









