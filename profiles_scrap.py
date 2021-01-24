import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

profiles = []
with urlopen("http://www.pollub.pl/pl/kandydaci/studia-i-stopnia/kierunki-ksztalcenia") as pollub_profiles:
    profile = pollub_profiles.read()

soup = BeautifulSoup(profile, 'html.parser')
rows = soup.div.find(id="mainContent").findAll("strong")
for row in rows:
    if "NOWY" in str(row.text):
        # usuwamy (NOWY KIERUNEK) z końca i puste linie następnie dodajemy wiersz do listy
        if str(row.text)[:-17:1] != "":
            profiles.append(str(row.text)[:-17:1])
    elif "." in str(row.text):
        # usuwamy tytuły profili
        continue
    else:
        # wpisujemy profil do listy
        profiles.append(str(row.text))

with open("json/profiles.json", "w") as pollub:
    json.dump(profiles, pollub, ensure_ascii=False, indent = 2)