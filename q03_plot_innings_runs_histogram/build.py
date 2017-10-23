# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution

def plot_innings_runs_histogram():
    ball_count=ipl_df[['match_code','delivery']]
    a=ipl_df['inning']==1
    b=ipl_df['inning']==2
    a_agg=ball_count[a]
    b_agg=ball_count[b]

    agg_ball_count=a_agg.groupby(['match_code']).agg('count')
    agg_ball_count_second=b_agg.groupby(['match_code']).agg('count')



    #print(agg_ball_count.head(5))

    run_count=ipl_df[['match_code','runs']]
    second_inning_agg_run =run_count[a]
    agg_ball_sum=second_inning_agg_run.groupby(['match_code']).agg('sum')
    #print(agg_ball_sum.head(5))
    df=pd.concat([agg_ball_sum],axis=1)
    #print(df.head(5))
    df.plot.hist()


    fig, axes = plot.subplots(nrows=1, ncols=2)
    #axes[0][1].plot.hist(df)
    #plot.sca(axes[0,0])
    #df.plot.hist()
    plot.show()
    #print(axes)

#plot_innings_runs_histogram()
#plot.hist(alpha=0.5)
