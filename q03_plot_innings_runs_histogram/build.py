# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innigs_runs_histogram():
    x=ipl_df[ipl_df['toss_decision']=='bat']['total']
    y=ipl_df[ipl_df['toss_decision']=='field']['total']
    fig, ax = plt.subplots(1,2)
    ax[0].hist(x, bins=10, alpha = 0.5, color = 'r')
    ax[1].hist(y, bins=10, alpha = 0.5, color = 'g')
    plt.show()
    
x=ipl_df[ipl_df['toss_decision']=='bat']['total']
y=ipl_df[ipl_df['toss_decision']=='field']['total']
plt.subplots(2,1)
plt.hist(y,bins=10)


# An 'interface' to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=x, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
fig, ax = plt.subplots(1,2)
ax[0].hist(x, bins=10, alpha = 0.5, color = 'r')
ax[1].hist(y, bins=10, alpha = 0.5, color = 'g')
plt.show()
plot_innigs_runs_histogram()


