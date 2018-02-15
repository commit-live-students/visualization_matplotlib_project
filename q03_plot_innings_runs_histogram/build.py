import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    match=ipl_df[['match_code','inning','batting_team','runs']]
    by_match=match.groupby(['match_code','inning','batting_team']).sum().reset_index()
    df_first_inning=by_match.loc[by_match['inning'] == 1].reset_index()
    df_second_inning=by_match.loc[by_match['inning'] == 2].reset_index()
    df_f_inn=df_first_inning[['match_code','runs']]
    df_s_inn=df_second_inning[['match_code','runs']]
    result=pd.merge(df_f_inn,df_s_inn,on='match_code')
    runs = pd.DataFrame(result, columns=['runs_x', 'runs_y'])
    ax=runs.plot(kind='hist')
    ax.legend(['1st','2nd'])
    plt.show()
