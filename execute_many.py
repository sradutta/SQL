import sqlite3 as lite

cities = (('Las Vegas', 'NV'),
          ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December'),
           ('Atlanta', 2013, 'July', 'January'))

con = lite.connect('getting_started.db')

with con:
  cur = con.cursor()
  cur.executemany("INSERT INTO cities VALUES(?, ?)", cities)
  #cur.executemany("INSERT INTO weather VALUES(?, ?, ?, ?)", weather)
