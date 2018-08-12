# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
df=ipl_df[['batting_team','match_code']]
count=df.groupby('batting_team').match_code.nunique()
count.plot.bar()
plt.show()



