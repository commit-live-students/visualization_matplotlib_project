# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

df=pd.DataFrame(ipl_df)
r=df.groupby('match_code').agg(np.sum)
plt.hist(r['runs'],bins=10)



