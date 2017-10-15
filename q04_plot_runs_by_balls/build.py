import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    a = ipl_df["runs"].groupby(ipl_df.batsman).sum()
    b = ipl_df["delivery"].groupby(ipl_df.batsman).sum()
    a=pd.DataFrame(a)

    b=pd.DataFrame(b)
    c = a.join(b)
    plt.scatter(c["delivery"],c["runs"])
    plt.title("deliveries vs runs")
    plt.xlabel("balls played")
    plt.ylabel("runs scores")
    plt.show()
plot_runs_by_balls()
