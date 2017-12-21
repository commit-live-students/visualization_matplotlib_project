import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    res1=ipl_df[ipl_df ['inning']==1]
    res2=ipl_df[ipl_df ['inning']==2]

    res_1=pd.DataFrame({'inning1' : res1.groupby(['match_code','inning'])['runs'].sum()}).reset_index()
    res_2=pd.DataFrame({'inning2' : res2.groupby(['match_code','inning'])['runs'].sum()}).reset_index()
    res_final=pd.merge(res_1, res_2, how='inner', on=['match_code'])
    plt.figure(figsize=(10,4))
    plt.subplot(121)
    sns.distplot(res_final['inning1'], kde=False)
    plt.subplot(122)
    sns.distplot(res_final['inning2'], kde=False)
    plt.tight_layout()
    plt.show()
