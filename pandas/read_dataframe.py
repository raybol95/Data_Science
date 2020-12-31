import pandas as pd
from sqlalchemy import create_engine 

df_csv = pd.read_csv('filename.csv') #read csv file
df_excel = pd.read_excel('filename.xlsx') # read excel file
df_json = pd.read_json('filename.json') # read json file
df_pickle = pd.read_pickle('filename.pkl') # read pickle file

connection = create_engine('postgresql://blablabla') # make a connection to database, in this case is postgreesql
df_sql = pd.read_sql('table_name', connection) # read data table from sql database
df_query = od.read_sql('select a from b where id>50', connection) # read data using a sql query
