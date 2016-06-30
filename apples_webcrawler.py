# coding=utf-8
import requests, bs4
import pprint

res = requests.get('http://www.sadbiznes.pl/notowania-jablek/7')
text = bs4.BeautifulSoup(res.text, "html.parser")

def get_column_data(data_selector, class_value_selector):
    results=[]
    for i in text.find_all(data_selector, class_=class_value_selector):
        results.append(i.string.strip())
    return results

selector_info = {
    "for_day":["td", "views-field views-field-changed"],
    "name": ["td", "views-field views-field-tid-3"],
    "note_day": ["span", "date-display-single"],
    "city": ["td", "views-field views-field-tid"],
    "price_min": ["td", "views-field views-field-field-cena-min-value"],
    "price_max": ["td", "views-field views-field-field-cena-max-value"]
}

col_dict = {}

for key_name, (selector_first, selector_second) in selector_info.iteritems():
    col_dict[key_name] = get_column_data(selector_first, selector_second)

pprint.pprint(col_dict)