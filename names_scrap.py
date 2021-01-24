import json
from urllib.request import urlopen      # urlopen wykorzystamy do przeglądania zawartości witryn
from bs4 import BeautifulSoup           # BeautifulSoup posłuży nam do poruszania się po dokumencie HTML
# Ze stony uzyskamy dane takie jak imie oraz ile razy takie imie wystąpiło 
# dlatego tworzymy listy w których te dane będziemy przechowywać
males_percent = []      # Lista z danymi do obliczenia prawdopodobieństwa wystąpienia imienia
females_percent = []
males = []              # Lista z imionami
females = []
# Przy pomocy urlopen otwieramy stronę a jej zawartość zapisujemy w zmiennej names
with urlopen("https://www.ssa.gov/oact/babynames/decades/century.html?format=json") as web_data:
    names = web_data.read()
# Parsujemy otrzymany dokument HTML wykorzystując narzędzie BeautifulSoup
soup = BeautifulSoup(names, 'html.parser')
# W dokumencie HTML przechodzimy odpowiednio do body(zawartość strony) => tbody(zawartość tabeli z danymi) =>
# => znajdujemy wszystkie komórki z danymi (znaczki <td>Imie</td> <td>Wartość</td>)
rows = (soup.body.tbody.findAll("td"))

# Dane z tabeli wykorzystamy do prawdopodobieństwa na wystąpienie danego imienia wśród studentów
# output rows wygląda tak: 
# <td>1</td>
# <td>James</td>
# <td>4,735,694</td>
# <td>Mary</td>
# <td>3,265,105</td>
# Dlatego aby poruszać sie tylko po wartościach imion męski zapiszemy rows[2:-2:5]
# Czyli zacznij od imion męskich aż do końca -2 (ponieważ 2 ostatnie linie zawierały informacje o tabeli),
# skacząc co 5
for row in rows[2:-2:5]:
    # Output row: <td>4,735,694</td> 
    # [4:-5:1] usuwa znaczniki a replce zamienia , na . abyśmy mogli przeparsować do float
    row = float(str(row)[4:-5:1].replace(',', ''))
    # Do listy z procentem na imię wpisujemy wartość która odpowiadać będzie szansie na dane imie
    if float(str(row)) > 4000000: 
        males_percent.append(5)
    elif float(str(row)) > 2000000: 
        males_percent.append(4)
    elif float(str(row)) > 1000000: 
        males_percent.append(3)
    elif float(str(row)) > 500000: 
        males_percent.append(2)
    else:
        males_percent.append(1)
# Analogicznie tyle, że dla imion źeńskich
for row in rows[4:-2:5]:
    row = float(str(row)[4:-5:1].replace(',',''))
    if float(str(row)) > 4000000: 
        females_percent.append(5)
    elif float(str(row)) > 2000000: 
        females_percent.append(4)
    elif float(str(row)) > 1000000: 
        females_percent.append(3)
    elif float(str(row)) > 500000: 
        females_percent.append(2)
    else:
        females_percent.append(1)

i = 0
# W oparciu o 'procent' wpisuujemy imiona do listy males[]
for row in rows[1:-2:5]:
    for chance in range(males_percent[i]):
        males.append(str(row)[4:-5:1])
    i += 1
    
i = 0
# W oparciu o 'procent' wpisuujemy imiona do listy females[]
for row in rows[3:-2:5]:
    for chance in range(females_percent[i]):
        females.append(str(row)[4:-5:1])
    i += 1
# Exportujemy nasze list jako pliki.json
with open("json/male_names.json", "w", encoding="utf-8") as export:
    json.dump(males, export, indent=4)
with open("json/female_names.json", "w", encoding="utf-8") as export:
    json.dump(females, export, indent=4)