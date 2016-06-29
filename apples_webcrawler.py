# coding=utf-8
import requests, bs4
res = requests.get('http://www.sadbiznes.pl/notowania-jablek/7')
text = bs4.BeautifulSoup(res.text, "html.parser")


def get_column_data(data_selector, class_value_selector):
    results=[]
    for i in text.find_all(data_selector, class_=class_value_selector):
        results.append(i.string.strip())
    return results


col_dict = {
    "for_day": [],
    "name": [],
    "note_day": [],
    "city": [],
    "price_min": [],
    "price_max": []
}

selector_info = {
    "for_day":["td", "views-field views-field-changed"],
    "name": ["td", "views-field views-field-tid-3"],
    "note_day": ["span", "date-display-single"],
    "city": ["td", "views-field views-field-tid"],
    "price_min": ["td", "views-field views-field-field-cena-min-value"],
    "price_max": ["td", "views-field views-field-field-cena-max-value"]
}

for i in col_dict:
    s = 0
    for selector in selector_info:
        col_dict[i] = get_column_data(selector_info.items()[s][1][0], selector_info.items()[s][1][1])
        s = s + 1

print col_dict


print selector_info.items()[0][1][0]
print selector_info.items()[0][1][1]