# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')


ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team(ipl_df=ipl_df):
    ipl_df['batting_team'].value_counts().plot.bar()
plot_deliveries_by_team()





