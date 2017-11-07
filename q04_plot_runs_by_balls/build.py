
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    c = ipl_df.groupby(['match_code','batsman'])['match_code'].count()
    d = ipl_df.groupby(['match_code','batsman'])['runs'].sum()
    a1 = pd.DataFrame(c)
    b1 = pd.DataFrame(d)
    a1 =  a1.join(b1)
    plt.scatter(a1['match_code'],a1['runs'])
    plt.title("ball vs runs per match/innings")
    plt.xlabel("balls")
    plt.ylabel("runs")
    plt.show()
plot_runs_by_balls()
