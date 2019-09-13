import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def  plot_matches_by_team():
    ipl_df.groupby("batting_team").agg({'match_code':"nunique"}).plot(kind='bar')
    plt.show()
