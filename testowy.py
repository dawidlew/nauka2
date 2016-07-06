# coding=utf-8
import time
import sqlite3

conn = sqlite3.connect('apples_webcrawler.db')
cursor = conn.cursor()
timestamp = time.time()
print int(timestamp)


avg_price = cursor.execute(
    "select DISTINCT name, city, round(avg(replace(price_min, ',', '.')),2), "
    "round(avg(replace(price_max, ',', '.')),2) from note "
    "where for_day in (select DISTINCT for_day from note order by for_day desc limit 10) "
    "group by name, city")
avg_price_data = avg_price.fetchall()

print avg_price_data




avg_price_1 = cursor.execute(
    "select DISTINCT for_day from note order by for_day desc limit 10")
avg_price_data_1 = avg_price_1.fetchall()

print avg_price_data_1



cursor.close()