# coding=utf-8
import time
import sqlite3

conn = sqlite3.connect('apples_webcrawler.db')
cursor = conn.cursor()

# cursor.execute("drop table note_agg")
# cursor.execute("create table note_agg (name, city, avg_price_min, avg_price_max, timestamp)"

avg_price_data = cursor.execute("select city, name, avg(price_min) as avg_price_min, avg(price_max) as avg_price_max" +
                                " from note group by city, name order by timestamp limit 10")
print(str(avg_price_data.fetchall()))


timestamp = time.time()

for values in (str(avg_price_data.fetchall())):
    cursor.execute('INSERT INTO note_agg (city, name, avg_price_min, avg_price_max) ' +
                   'VALUES (:city, :name, :avg_price_min, :avg_price_max)', (str(avg_price_data.fetchall())))

conn.commit()










results = cursor.execute("select * from note_agg")
print(str(results.fetchall()))

conn.close()

