import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    df1 = ipl_df.loc[:,['batsman','delivery','runs']]
    df2 = df1.loc[:,['batsman','runs']]
    df6 = df2.groupby(['batsman']).sum()
    #df2 = df2.fillna(0)
    #df2 = df2.sum(axis=1)
    df3 = df1.loc[:,['batsman','delivery']]
    df4 = df3.groupby(['batsman']).count()
    df5 = pd.concat([df6,df4],axis=1)
    df5.plot(x='delivery',y='runs',kind='scatter')
    plt.show()
