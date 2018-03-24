import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_innings_runs_histogram():
    total_runs = ipl_df.groupby(['inning','match_code']).agg({'runs':['sum']}).reset_index()
    first_inning_data = total_runs[total_runs['inning'] == 1]
    second_inning_data = total_runs[total_runs['inning'] == 2]
    fig = plt.figure()
    fig.add_subplot(121)
    plt.hist((first_inning_data.iloc[:,first_inning_data.columns.get_level_values(1)=='sum']).values)
    plt.title('IPL 1st inning')
    plt.xlabel('Runs')
    plt.ylabel('Frequency')
    fig.add_subplot(122)
    plt.hist((second_inning_data.iloc[:,second_inning_data.columns.get_level_values(1)=='sum']).values)
    plt.title('IPL 2nd inning')
    plt.xlabel('Runs')
    plt.ylabel('Frequency')
    plt.show()



