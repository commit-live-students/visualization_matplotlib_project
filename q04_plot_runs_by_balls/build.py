import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    runs_scored = pd.DataFrame(ipl_df.groupby(['match_code', 'batsman']).agg('sum')['runs'])
    balls_played = pd.DataFrame(ipl_df.groupby(['match_code', 'batsman']).agg('count')['delivery'])
    playedscored = runs_scored.join(balls_played)
    plt.scatter(playedscored['runs'], playedscored['delivery'])
    plt.show();
    


plot_runs_by_balls()



