import pandas as pd

data = {'fruit':['apple', 'orange', 'grape', 'banana', 'pineapple'], 'value':[2,4,6,10,2]} # dictionary for column and row values
df = pd.DataFrame(data) #make a dataframe from data dictionary
df.head() #show first 5 rows of dataframe
