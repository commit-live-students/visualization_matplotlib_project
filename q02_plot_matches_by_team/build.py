# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


df=pd.DataFrame(ipl_df)
s=df.groupby('match_code').agg(pd.Series.nunique)
r=df.groupby('batting_team').agg(pd.Series.nunique)
a=list(r['match_code'].index)
b=list(r['match_code'])
plt.bar(a,b)




