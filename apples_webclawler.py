# coding=utf-8
import requests, bs4
res = requests.get('http://www.sadbiznes.pl/notowania-jablek/7')
text = bs4.BeautifulSoup(res.text, "html.parser")


# bla1 = text.select('td.views-field.views-field-tid-3')
# print 'bla1: %s' % bla1
#
# bla2 = text.find_all('td', class_="views-field views-field-changed")
# print 'bla2: %s' % bla2

# bla3 = text.html.head.title.string
# print 'bla3: %s' % bla3



var0 = "td"
var1 = "views-field views-field-changed"
var2 = "for_day"



dict1 = {var2: [], "name": [], "note_day": [], "city": [], "price_min": [], "price_max": []}

for i in text.find_all(var0, class_=var1):
    dict1[var2].append(i.string.strip())

for i in text.find_all('td', class_="views-field views-field-tid-3"):
    dict1["name"].append(i.string.strip())
for i in text.find_all('span', class_="date-display-single"):
    dict1["note_day"].append(i.string.strip())
for i in text.find_all('td', class_="views-field views-field-tid"):
    dict1["city"].append(i.string.strip())
for i in text.find_all('td', class_="views-field views-field-field-cena-min-value"):
    dict1["price_min"].append(i.string.strip())
for i in text.find_all('td', class_="views-field views-field-field-cena-max-value"):
    dict1["price_max"].append(i.string.strip())


print dict1

assert len(dict1["for_day"]) == len(dict1["name"])
assert len(dict1["note_day"]) == len(dict1["name"])



