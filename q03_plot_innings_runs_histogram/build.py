import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
plot_innings_runs_histogram():
    data = ipl_df.groupby(['match_code','inning'])
    data['inning'].count().plot(kind='bar')
    plt.show()
