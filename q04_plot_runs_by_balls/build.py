import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    no_of_delivery = ipl_df.delivery
    no_of_runs = ipl_df.runs
    plt.scatter(no_of_delivery, no_of_runs)
    plt.show()

plot_runs_by_balls()    
