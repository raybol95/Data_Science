import pandas as pd

df = pd.read_csv('filename.csv')
df.head() # checking the first 5 rows dataframe.
df.shape # checking the dimension of dataframe
df.info() # give an information about dataset per column
df.describe() # give a statistic information of dataset
