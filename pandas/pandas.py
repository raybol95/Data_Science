import pandas as pd

data = {'fruit':['banana', 'apple', 'grape', 'orange', 'durian', 'pineapple'], 'value':[10, 5, 40, 12, 2, 4]} # make a dictionary data with columns and rows
df = pd.DataFrame(data) # convert dictionary data to dataframe with pandas
df.head() # show first 5 rows dataframe
