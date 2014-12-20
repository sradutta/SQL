#the sqlite3 module is used to work with the sqlite data
import sqlite3 as lite

#here you connect to the database. The connect method returns
#a connection object
con = lite.connect('getting_started.db')
 
with con:
 #from the connection, you get a cursor object. The cursor is 
 #what goes over the recors that results from the query
 cur = con.cursor()
 cur.execute('SELECT SQLITE_VERSION()')
 
 #you're fetching the data fromt the cursor object. Use fetchone
 #for fetching one method; fetchall for fetching more than 1 method
 data = cur.fetchone()

 #finally print the result
 print "SQLIte version: %s" %data
