## Create a bar plot of the total number of deliveries played by each team across all matches in the dataset

Let's start with a simple task.

You need to write a function `plot_deliveries_by_team()` which creates a bar plot of team names (batting_team) on the X axis, and their respective counts of deliveries played on the Y axis.

## Parameters:
This function takes in no parameters

## Returns
This function returns nothing
### Hint

* What is needed here is essentially a "batting_team" vs "count of deliveries" 
* if you provide 'count()' as aggregator to the groupby().agg(aggregator), it will give you counts of deliveries
