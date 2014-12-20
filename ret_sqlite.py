import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:
  cur = con.cursor()
  cur.execute("SELECT * FROM cities")

  rows = cur.fetchall()
  for row in rows:
      print row
