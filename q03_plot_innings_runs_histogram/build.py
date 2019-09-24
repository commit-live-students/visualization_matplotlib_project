import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    gdf_ipl_1 = ipl_df.groupby(by=['match_code','inning'],as_index=False)
    df_match_inning_sum = gdf_ipl_1['runs'].sum()
    print df_match_inning_sum.head()
    # First inning runs
    plt.subplot(1,2,1)
    first_ing_scores = df_match_inning_sum[df_match_inning_sum['inning'] == 1].runs
    ax_first = first_ing_scores.plot(kind='hist',grid=True)
    ax_first.set_title("First Innings Runs")
    ax_first.set_xlabel("First Inning Runs Scored")
    ax_first.set_ylabel("Number of matches")
    # Second inning runs
    plt.subplot(1,2,2)
    second_ing_scores = df_match_inning_sum[df_match_inning_sum['inning'] == 2].runs
    ax_second = second_ing_scores.plot(kind='hist',grid=True)
    ax_second.set_title("Second Innings Runs")
    ax_second.set_xlabel("Second Inning Runs Scored")
    ax_second.set_ylabel("Number of matches")

    plt.tight_layout()
    plt.show()
