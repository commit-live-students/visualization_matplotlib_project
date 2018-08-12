import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
df=ipl_df[['batting_team','match_code']].groupby('batting_team')['match_code'].nunique().plot.bar()
plt.show()
