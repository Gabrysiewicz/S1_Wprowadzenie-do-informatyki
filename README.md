<h1 align='center'> Projekt z przedmiotu "Wprowadzenie do informatyki" </h1>

### Cel: Utworzenie projektu w Python wykorzysatującego JSON oraz WebScrapping do wygenerowania danych na potrzeby bazy danych
### Stan: Outdated
<hr>

### Opis
Repozytorium z pierwszego projektu na pierwszym semestrze w Politechnice Lubelskiej. 
Projekt generował pliki json z informacji ze strony www o najpopularniejszych imionach męskich i żeńskich oraz dostępnych profilach kształcenia na Politechnice Lubelskiej.
Następnie z wygenerowanych plików JSON powstawał jeden wynikowy plik z danymi które można było wykorzystać w bazie danych:

Fragment kody z `generator.py` który dla podanej liczby `900` najpierw losowo wybierał płeć, następnie pobierał imie na bazie płci i wypełniał `dict` Database z którego finalnie generwano plik `pollub_db_json`
``` 
for i in range(900):
    sex = int(random.random() * 2)
    if sex == 0:
        male_name = male_names[int(random.random() * len(male_names))]
        surname = sur_names[int(random.random() * len(sur_names))]
        index = random_index()
        DataBase['student'].append({
            "name": "" + male_name + "",
            "surname": "" + surname + "",
            "age": "" + random_student_age() + "",
            "sex": "M",
            "tel": "+48 " + random_tel() + "",
            "email": "s" + index + "@pollub.edu.pl",
            "address": {
                "city": ""+random_city()+"",
                "street": "Piłsudskiego",
                "number": "" + random_number() + ""
            },
            "index": "" + "0" + index + "",
            "year": "" + random_year() + "",
            "profile": "" + random_profile() + ""
        })
    else:
        female_name = female_names[int(random.random() * len(female_names))]
        surname = sur_names[int(random.random() * len(sur_names))]
        index = random_index()
        DataBase['student'].append({
            "name": "" + female_name + "",
            "surname": "" + surname + "",
            "age": "" + random_student_age() + "",
            "sex": "F",
            "tel": "+48 " + random_tel() + "",
            "email": "s" + index + "@pollub.edu.pl",
            "address": {
                "city": ""+random_city()+"",
                "street": "Piłsudskiego",
                "number": "" + random_number() + ""
            },
            "index": "" + "0" + index + "",
            "year": "" + random_year() + "",
            "profile": "" + random_profile() + ""
        })

```

<hr>

### Uwagi
Projekt dotyczył głównie zastosowania języka Python dlatego z jakies powodu nie ma tutaj ręcznego pliku z nazwami miast oraz exportu bazy i schematu bazy danych
