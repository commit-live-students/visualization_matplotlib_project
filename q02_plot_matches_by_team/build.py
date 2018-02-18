import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    df1 = ipl_df.loc[:,['match_code', 'batting_team']]
    n_mc = np.unique(df1.loc[:,'match_code'])
    n_bt = np.unique(df1.loc[:,'batting_team'])
    dict1 = {}
    for val in n_bt:
        dict1[val] = 0

    for val in n_mc:
        df_temp = df1[df1.loc[:,'match_code'] == val]
        ind = df_temp.index.tolist()
        dict1[df_temp.loc[ind[0],'batting_team']] = dict1[df_temp.loc[ind[0],'batting_team']] + 1

    df2 = pd.DataFrame.from_dict(dict1,orient='index')
    df2.plot(kind='bar')
    plt.show()
