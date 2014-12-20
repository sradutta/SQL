
import sqlite3 as lite
import pandas as pd
con = lite.connect('/Users/kuttush/Desktop/Spongebob/Thinkful/DataScience/SQL/getting_started.db')
query_cities = "select * from cities"
cities = pd.read_sql(query_cities,con)
