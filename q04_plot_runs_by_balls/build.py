import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    total_runs = ipl_df.groupby(['inning','match_code','batsman']).agg({'runs':['sum'],'delivery':['count']}).reset_index()
    plt.scatter((total_runs.iloc[:,total_runs.columns.get_level_values(1)=='count']).values,(total_runs.iloc[:,total_runs.columns.get_level_values(1)=='sum']).values)
    plt.title('Count of balls vs runs scored, IPL')
    plt.xlabel('Count of Balls played')
    plt.ylabel('Total Runs scored')
    plt.show()
