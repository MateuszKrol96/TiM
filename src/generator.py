import random
from random import choice, choices

from src import data_names
from src import data_districts
from collections import Counter

import numpy as np


def generate_people(number=25):
    """
    Function for generating people
    
    :param int number: Number of names to generate
    :return: list of names
    :rtype: list
    """
    wroclaw_population = 653157
    list_first_names_m = data_names.FIRST_NAMES_M
    list_second_names_m = data_names.LAST_NAMES_M
    list_first_names_f = data_names.FIRST_NAMES_F
    list_second_names_f = data_names.LAST_NAMES_F
    district_population = data_districts.DISTRICTS
    wages_districts = [41, 43, 22, 3, 9, 48, 17, 14, 20, 27, 12, 56, 9, 5, 1, 22,
                       12, 34, 36, 9, 10, 32, 9, 10, 48, 37, 10, 9, 56, 10, 3, 2,
                       5, 3, 7, 49, 5, 10, 1, 2, 24, 17, 34, 37, 41, 58, 24, 7
                       ]
    out_of_city = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    age = np.arange(18, 72)
    genders = ["M", "K"]
    names_list = []
    for e in range(number):
        gender = random.choices(genders, weights = [18, 25], k= 1)[0]
        if gender == "M":
            temp_name = choice(list_first_names_m)
            temp_surname = choice(list_second_names_m)
        else:
            temp_name = choice(list_first_names_f)
            temp_surname = choice(list_second_names_f)
        if number < wroclaw_population and (choice(out_of_city)) == 0:
            temp_home_district = choices(district_population, wages_districts)[0]
        else:
            temp_home_district = "NIE WROCLAW"

        if choice(out_of_city) == 0:
            temp_work_district = choices(district_population, wages_districts)[0]
        else:
            temp_work_district = "NIE WROCLAW"

        if choice(out_of_city) == 0:
            temp_fun_district = choices(district_population, wages_districts)[0]
        else:
            temp_fun_district = "NIE WROCLAW"

        temp_age = round(random.randint(18,71))
        temp_person = {
            "ID": e + 1,
            "Imie": temp_name,
            "Nazwisko": temp_surname,
            "Wiek": temp_age,
            "plec": gender,
            "dom": temp_home_district,
            "praca": temp_work_district,
            "rozrywka": temp_fun_district}
        names_list.append(temp_person)

    return names_list


def generate_peoples_journeys(people):
    transport_medium = ["car", "car", "tram", "bus", "bike", "car", "car", "car", "car", "on foot"]
    for e in people:
        e['podroze'] = {}
        if e.get('dom') != e.get('praca') and e.get('praca') != 'NIE WROCLAW':
            e['podroze']['dom-praca'] = choice(transport_medium)
        if e.get('dom') != e.get('rozrywka') and e.get('rozrywka') != 'NIE WROCLAW':
            # people.remove(e)
            e['podroze']['dom-rozrywka'] = choice(transport_medium)


def count_journeys(full_info):
    zaparkowania = {"praca": [], "rozrywka": []}
    for e in full_info:
        if 'dom-praca' in e['podroze']:
            zaparkowania['praca'].append(e['praca'])
        if 'dom-rozrywka' in e['podroze']:
            zaparkowania['rozrywka'].append(e['rozrywka'])
    full_list = {"praca": {}, "rozrywka": {}}
    t_list = dict(Counter(zaparkowania['praca']))
    full_list['praca'] = dict(sorted(t_list.items(), key=lambda x: x[1], reverse=True))

    t_list = dict(Counter(zaparkowania['rozrywka']))
    full_list['rozrywka'] = dict(sorted(t_list.items(), key=lambda x: x[1], reverse=True))
    # print(full_list)
    return full_list

def generate_peoples_opinions(people, parking_occupation):
    for e in people:
        basic_opinion = round(random.uniform(0.5, 1),2)
        work = e.get('praca')
        fun = e.get('rozrywka')
        if not work == 'NIE WROCLAW':
            if parking_occupation.get(work) > 10:
                basic_opinion -= 0.2
            elif 1 < parking_occupation.get(work) < 10:
                basic_opinion -= 0.1
        if not fun == 'NIE WROCLAW':
            if parking_occupation.get(fun) > 10:
                basic_opinion -= 0.2
            elif 1 < parking_occupation.get(fun) < 10:
                basic_opinion -= 0.1
        e['opinion'] = round(basic_opinion, 2)
    return people


