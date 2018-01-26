import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    path = "./data/ipl_dataset.csv"
    df = pd.read_csv(path)
    fig, ax = plt.subplots()
    df['batting_team'].value_counts().plot(ax=ax, kind='bar')
