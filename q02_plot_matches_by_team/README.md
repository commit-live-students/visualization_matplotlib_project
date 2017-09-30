## Create a bar plot of the total number of matches played by each team

You need to write a function `plot_matches_by_team()` which creates a bar plot of team names (batting_team) on the X axis, and their respective counts of matches played on the Y axis.

You don't have to work with columns `team1` and `team2`, you can assume each team bats and just work with `batting_team` instead.

## Parameters:
This function takes in no parameters

## Returns
This function returns nothing

## Hints
- What is needed here is essentially a "batting_team" vs "unique/distinct count of matches"
- if you provide 'nunique' as aggregator to the groupby().agg(aggregator), it will give you unique counts