import sqlite3 as lite
import pandas as pd

def test1(con):
    with con:
      cur = con.cursor()
      cur.execute("SELECT * FROM cities")
      rows = cur.fetchall()
      cols = [desc[0] for desc in cur.description]
      df = pd.DataFrame(rows, columns=cols)
      return df
con = lite.connect('/Users/kuttush/Desktop/Spongebob/Thinkful/DataScience/SQL/getting_started.db')      
x = test1(con)
print x
