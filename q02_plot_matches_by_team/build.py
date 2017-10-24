import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('./data/ipl_dataset.csv', index_col=None)


def plot_matches_by_team():
    fig,ax = plt.subplots()
    ipl_df.groupby(['batting_team'])['match_code'].nunique().plot(ax=ax,kind='bar')
