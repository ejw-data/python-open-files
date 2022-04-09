
# Outline Opening Files in Python


## with open()


## f = open()



import pandas as pd

# used for delimited files
df = pd.read_csv()
# text file of fixed width content
df = pd.read_fwf()  # example - census files
# common data file type, common like .csv
df = pd.read_parquet()
# less used data file type
df = pd.read_pickle()

# SQL
df = pd.read_sql()
df = pd.read_sql_table()
df = pd.read_sql_query()

# Read web files
df = pd.read_json()
df = pd.read_html() # - not sure how useful

# load data from Google BigQuery
df = pd.read_gbq()  

# reads other software files
df = pd.read_excel()
df = pd.read_sas()
df = pd.read_spss()
df = pd.read_stata()




