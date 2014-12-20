import sqlite3 as lite
import pandas as pd

con = lite.connect('/Users/kuttush/Desktop/Spongebob/Thinkful/DataScience/SQL/getting_started.db')

with con:
   cur = con.cursor()
   cur.execute("SELECT * FROM cities")

with con:
   cur = con.cursor()
   cur.execute("SELECT * FROM cities")

   rows = cur.fetchall()
   df = pd.DataFrame(rows)
