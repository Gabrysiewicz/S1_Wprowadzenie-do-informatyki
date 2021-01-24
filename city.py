import json

cities = []
with open("json/miasta.json") as city:
    data = json.load(city)
for i in range(len(data)):
    for item in data[i]['cities']:
        # print(item['text_simple'])
        cities.append(item['text_simple'])

with open("json/cities.json", 'w') as export:
    json.dump(cities, export, ensure_ascii=False)