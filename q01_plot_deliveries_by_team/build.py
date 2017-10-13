import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def plot_deliveries_by_team() :
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    #ipl_df[['batting_team']].plot.bar()
    data = ipl_df.groupby(["batting_team"])['delivery'].count()
    #data = ipl_df.groupby('batting_team').delivery.agg(['count']).reset_index(name='count')
    #data = ipl_df.groupby(['batting_team').delivery.agg(['count']).reset_index(name='count')
    #data = ipl_df.sort_index(['batting_team']) ['delivery'].sum()
    data = data.reset_index().sort_values(['delivery'],ascending=False).set_index(['batting_team'])
    #print data
    data.plot.bar(legend=False)
    plt.show()


# Solution
