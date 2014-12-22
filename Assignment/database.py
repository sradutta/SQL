#import libraries
import sqlite3 as lite
import pandas as pd

#create the data-set as tuples
cities = (('New York City', 'NY'), 
          ('Boston', 'MA'),
          ('Chicago', 'IL'),
          ('Miami', 'FL'),
          ('Dallas', 'TX'),
          ('Seattle', 'WA'),
          ('Portland', 'OR'),
          ('San Francisco', 'CA'),
          ('Los Angeles', 'CA'))

weather = (('New York City', 2013, 'July', 'January', 62),
           ('Boston', 2013, 'July', 'January', 59),
           ('Chicago', 2013, 'July', 'January', 59),
           ('Miami', 2013, 'August', 'January', 84),
           ('Dallas', 2013, 'July', 'January', 77),
           ('Seattle', 2013, 'July', 'January', 61),
           ('Portland', 2013, 'July', 'December', 63),
           ('San Francisco', 2013, 'September', 'December', 64),
           ('Los Angeles', 2013, 'September', 'December', 75))

con = lite.connect('getting_started.db')
with con:
   cur = con.cursor()
   cur.executemany("INSERT INTO cities VALUES (?,?)", cities)
   cur.executemany("INSERT INTO weather VALUES (?,?,?,?,?)", weather)

   cur.execute("SELECT * FROM cities")
   rowscities = cur.fetchall()
   colscities = [desc[0] for desc in cur.description]
   dfcities = pd.DataFrame(rowscities,columns=colscities)

   cur.execute("SELECT * FROM weather")
   rowsweather = cur.fetchall()
   colsweather = [desc[0] for desc in cur.description]
   dfweather = pd.DataFrame(rowsweather,columns=colsweather)

   #the assignment is asking for joining the data together. 
   #So, I'm going to use both inner and outer join of Panda
   #Here it might not matter as both tables are same 
   innerjoin = pd.merge(dfcities, dfweather, on='city', how='inner')
   outerjoin = pd.merge(dfcities, dfweather, on='city', how='outer')

#query_cities = "INSERT INTO cities VALUES (?,?)", cities
#everything_cities = pd.io.sql.write_frame(query_cities, con)

#query_weather = "INSERT INTO weather VALUES (?,?,?,?,?)", weather
#everything_cities = pd.read_sql(query_weather, con)

query_combined = "select * from cities c join weather w on c.city = w.city"
everything = pd.read_sql(query_combined,con)
print(everything)
