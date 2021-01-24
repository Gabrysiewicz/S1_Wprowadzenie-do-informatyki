import json
import random

with open("json/male_names.json", 'r', encoding="utf-8") as males_json:
    male_names = json.load(males_json)
with open("json/female_names.json", 'r', encoding="utf-8") as females_json:
    female_names = json.load(females_json)
with open("json/surnames.json", 'r', encoding="utf-8") as surnames_json:
    sur_names = json.load(surnames_json)
with open("json/profiles.json", 'r', encoding="utf-8") as profiles_json:
    profiles = json.load(profiles_json)
with open("json/towns.json", 'r') as towns_json:
    towns = json.load(towns_json)

# Losowe miasto
def random_city():
    chance = int(random.random()*100)
    town = "Lublin"
    if chance < 60:
        town = towns[int(random.random()*len(towns))]
    return town
# Losowy liczba, argument = max range, return type = string
def max_rnd_str(n):
    result = str(int(random.random() * n))
    return result
# return type = int
def random_number():
    number = max_rnd_str(1000)
    return number
# losowy numer telefonu
def random_tel():
    tel = ""
    for i in range(1, 13):
        if i % 4 == 0:
            tel += " "
        else:
            tel += max_rnd_str(10)
    return tel
# Losowy index
def random_index():
    index = max_rnd_str(100000)
    return index
# Losowa nazwa profilu
def random_profile():
    nr = int(random.random() * len(profiles))
    profile = profiles[nr]
    return profile
# Losowy wiek
def random_student_age():
    age = str(int(random.random() * 10) + 18)
    return age
def random_lecturer_age():
    age = str(int(random.random() * 20) + 30)
    return age
# Losowy rok 1-4
def random_year():
    year = str(int(random.random() * 4) + 1)
    return year
# Generator maila wykładowcy
def lecturer_email(name, surname):
    email = name[0:1].lower() + '.' + surname.lower()
    return email


DataBase = {'student': [], 'lecturer': []}

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

for i in range(50):
    sex = int(random.random() * 2)
    if sex == 0:
        name = male_names[int(random.random() * len(male_names))]
        surname = sur_names[int(random.random() * len(sur_names))]
        DataBase['lecturer'].append({
            "name": "" + name + "",
            "surname": "" + surname + "",
            "age": "" + random_lecturer_age() + "",
            "sex": "M",
            "tel": "+48 " + random_tel() + "",
            "email": "" + lecturer_email(name, surname) + "@pollub.pl",
            "address": {
                "city": "Lublin",
                "street": "Piłsudskiego",
                "number": "" + random_number() + ""
            },
            "profile": "" + random_profile() + ""
        })
    else:
        name = female_names[int(random.random() * len(female_names))]
        surname = sur_names[int(random.random() * len(sur_names))]
        DataBase['lecturer'].append({
            "name": "" + name + "",
            "surname": "" + surname + "",
            "age": "" + random_lecturer_age() + "",
            "sex": "M",
            "tel": "+48 " + random_tel() + "",
            "email": "" + lecturer_email(name, surname) + "@pollub.pl",
            "address": {
                "city": "Lublin",
                "street": "Piłsudskiego",
                "number": "" + random_number() + ""
            },
            "profile": "" + random_profile() + ""
        })
with open("json/pollub_db.json", 'w') as pollub_db_json:
    json.dump(DataBase, pollub_db_json, ensure_ascii=False, indent=2)
