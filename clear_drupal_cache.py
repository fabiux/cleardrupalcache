"""
Clear all Drupal cache entries.
Author: Fabio Pani <fabiux AT fabiopani DOT it>
License: see LICENSE
"""
import MySQLdb as DbLib

dbhost = 'localhost'
dbname = 'DRUPAL_DATABASE_NAME'
dbuser = 'DATABASE_USER'
dbpass = 'DATABASE_PASSWORD'

db = DbLib.connect(dbhost, dbuser, dbpass, dbname)
cursor = db.cursor()

cursor.execute("SHOW TABLES LIKE %s", ["cache%"])
cache_list = list(cursor.fetchall())
for table in cache_list:
    print 'Cleaning up table `' + table[0] + '`'
    cursor.execute("DELETE FROM " + table[0], ())
db.commit()
