import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)
#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    unique_match = ipl_df.groupby(['match_code','batting_team']).size().reset_index(name='count')

    batting_team = unique_match['batting_team'].value_counts()
    plt.bar(np.arange(len(batting_team)),batting_team)
    plt.xticks(np.arange(len(batting_team)),batting_team.index)
    plt.show()

# Solution
