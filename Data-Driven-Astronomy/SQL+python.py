#sudo ln -s /tmp/.s.PGSQL.5432 /var/run/postgresql/.s.PGSQL.5432

import psycopg2
#import sqlite3

def select_all(table):
  #conn = sqlite3.connect("init.db")
  #conn = psycopg2.connect(dbname='db')
  conn = psycopg2.connect(host='tatianaacerocuellar', user = 'postgres', password = 'postgres',database = "db")
  cursor = conn.cursor()
  query = 'SELECT * FROM ' + table + ';'

  cursor.execute(query)
  records = cursor.fetchall()

  return records

select_all('Star')
