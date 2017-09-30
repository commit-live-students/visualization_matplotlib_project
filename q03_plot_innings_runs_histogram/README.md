## Imagine you're the team captain. You need to decide whether to bat or field after a toss win.

Since you're also a data science enthusiast, you want this to be a data-driven decision. Clearly what you need to find is whether teams make better runs in the first inning or the second one. Maybe plotting distribution of runs (per inning per match) would help?

You need to plot a histogram to find the distribution of runs in 1st and 2nd innings. Write a function `plot_innings_runs_histogram()` which creates a figure with 2 subplots (shape: 1 row, 2 cols), and plots into them the histograms of runs made the first and second innings in each match respectively

## Parameters:
This function takes in no parameters

## Returns
This function returns nothing


## Hint:
Remember, what we want is the count of balls played (aggregation) and sum of runs (aggregation), per match per player (grouping). Since there is one grouping, and two different aggregations, you might want to "merge" them into one dataframe.