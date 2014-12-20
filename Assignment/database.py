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
          ('Portland' 'OR'),
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
   #executemany is not working because it works with only sqlite version 3.8 or higher. 
   #My sqlite3 is 3.8.7.4 but python is still using its default sqlite which is 3.7. 
   #I don't know how to make python use the newer version. 
   #Thus, I'm going to enter the values in another way.'
   #cur.executemany("INSERT INTO cities VALUES (?,?)", cities)
   #cur.executemany("INSERT INTO weather VALUES (?,?,?,?,?)", weather)

   #this is the way I'm entering the values until I resolve the above problem.
   cur.execute("INSERT INTO cities VALUES ('New York City', 'NY')")
   cur.execute("INSERT INTO cities VALUES ('Boston', 'MA')")
   cur.execute("INSERT INTO cities VALUES ('Chicago', 'IL')")
   cur.execute("INSERT INTO cities VALUES ('Miami', 'FL')")
   cur.execute("INSERT INTO cities VALUES ('Dallas', 'TX')")
   cur.execute("INSERT INTO cities VALUES ('Seattle', 'WA')")
   cur.execute("INSERT INTO cities VALUES ('Portland', 'OR')")
   cur.execute("INSERT INTO cities VALUES ('San Francisco', 'CA')")
   cur.execute("INSERT INTO cities VALUES ('Los Angeles', 'CA')")
   cur.execute("INSERT INTO weather VALUES ('New York City', 2013, 'July', 'January', 62)")
   cur.execute("INSERT INTO weather VALUES ('Boston', 2013, 'July', 'January', 59)")
   cur.execute("INSERT INTO weather VALUES ('Chicago', 2013, 'July', 'January', 59)")
   cur.execute("INSERT INTO weather VALUES ('Miami', 2013, 'August', 'January', 84)")
   cur.execute("INSERT INTO weather VALUES ('Dallas', 2013, 'July', 'January', 77)")
   cur.execute("INSERT INTO weather VALUES ('Seattle', 2013, 'July', 'January', 61)")
   cur.execute("INSERT INTO weather VALUES ('Portland', 2013, 'July', 'December', 63)")
   cur.execute("INSERT INTO weather VALUES ('San Francisco', 2013, 'September', 'December', 64)")
   cur.execute("INSERT INTO weather VALUES ('Los Angeles', 2013, 'September', 'December', 75)")

   cur.execute("SELECT * FROM cities")
   rowscities = cur.fetchall()
   colscities = [desc[0] for desc in cur.description]
   dfcities = pd.DataFrame(rowscities,columns=colscities)

   cur.execute("SELECT * FROM weather")
   rowsweather = cur.fetchall()
   colsweather = [desc[0] for desc in cur.description]
   dfweather = pd.DataFrame(rowsweather,columns=colsweather)



