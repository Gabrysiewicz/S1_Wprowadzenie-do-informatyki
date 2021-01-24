import json

with open("json/miasta.json","r") as towns_json:
    towns = json.load(towns_json)
print(json.dumps(towns,indent = 4,ensure_ascii=False))