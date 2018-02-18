import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    n1 = np.unique(ipl_df.loc[:,'team1'])
    n2 = np.unique(ipl_df.loc[:,'team2'])
    n3 = np.union1d(n1,n2)
    dict1 = {}
    for val in n3:
        df_temp = ipl_df[(ipl_df.loc[:,'toss_winner'] == val) & (ipl_df.loc[:,'toss_decision'] == 'bat')]
        df_temp1 = ipl_df[(((ipl_df.loc[:,'team1'] == val) | (ipl_df.loc[:,'team2'] == val)) & ((ipl_df.loc[:,'toss_winner'] != val) & (ipl_df.loc[:,'toss_decision'] != 'bat')))]
        df_temp2 = pd.concat([df_temp, df_temp1])
        dict1[val] = int(df_temp2.shape[0])

    df1 = pd.DataFrame.from_dict(dict1,orient='index')
    df1.plot(kind='bar')
    plt.show()
