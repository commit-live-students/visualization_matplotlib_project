# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    ipl=ipl_df.groupby('batting_team').agg({'match_code':'nunique'}).reset_index()
    ipl.plot(kind='bar')
    plt.xticks(index,list(ipl['batting_team']))
    plt.xlabel('Batting team')
    plt.ylabel('matches_played')
    plt.show()

values = ipl_df['batting_team'].value_counts().keys().tolist()
counts = ipl_df['batting_team'].value_counts().tolist()
ipl_df.groupby('match_code').agg({'batting_team':pd.Series.nunique})
counts
unique,counts=np.unique(arr,return_counts=True)
unique
d=dict(zip(unique,counts))
d
values
counts
arr=ipl_df['batting_team'].values
arr
arr.size
ipl_df.groupby('match_code')['batting_team'].nunique()
type(ipl)
ipl=ipl_df.groupby('match_code')['batting_team'].agg({'batting_team':'nunique'})
ipl
ipl.iloc[0,1]
ipl=ipl_df.groupby('match_code')
ipl
ipl
ipl
ipl_df
ipl=ipl_df.groupby(['match_code').agg('nunique')
ipl
ipl=ipl_df.groupby(['match_code']).value_counts().keys().tolist()
ipl
ipl['batting_team'].nunique()
ipl_df.groupby(['match_code']).agg({'batting_team':lambda x:x['batting_team']})
type(i)
i
i.nunique
i.nunique
ipl=ipl_df.groupby('batting_team').agg({'match_code':'nunique'}).reset_index()
ipl
ipl.plot(kind='bar')


