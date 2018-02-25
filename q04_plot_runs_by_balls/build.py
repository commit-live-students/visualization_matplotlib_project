import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    # Get the delivery count per batsman
    df_del_count = ipl_df[['batsman','delivery','runs']]\
                    .groupby(['batsman'])[['delivery']].count()
    # Get the total runs scored by batsman
    df_runs_total = ipl_df[['batsman','delivery','runs']]\
                    .groupby(['batsman'])[['runs']].sum()

    # Merge the DataFrame  (index as batsman)
    df_merged = pd.merge(df_del_count, df_runs_total,left_index=True, right_index=True)
    ax = df_merged.plot(kind='scatter',x='delivery',y='runs',grid=True)
    ax.set_title("Total Runs Scored against Number of Deliveries")
    ax.set_xlabel("Number of Deliveries")
    ax.set_ylabel("Total Runs Scored")
    plt.show()
