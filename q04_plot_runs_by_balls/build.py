# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    plt.scatter(ipl_df['runs'],ipl_df.index)
    plt.show()
    

plt.scatter(ipl_df['runs'],ipl_df.index)
plt.show()
fig, ax = plt.subplots(1,2)
ax[0].hist(x, bins=10, alpha = 0.5, color = 'r')
ax[1].hist(y, bins=10, alpha = 0.5, color = 'g')
plt.show()
plot_runs_by_balls()


