from random import choice, choices

import numpy

from src import data_names
from src import data_corpos
from src import data_districts

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
    out_of_city = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    age = np.arange(18, 70)
    genders = ["M", "K"]

    names_list = []
    for e in range(number):
        gender = choice(genders)
        if gender == "M":
            temp_name = choice(list_first_names_m)
            temp_surname = choice(list_second_names_m)
        else:
            temp_name = choice(list_first_names_f)
            temp_surname = choice(list_second_names_f)
        if number < wroclaw_population and (choice(out_of_city)) == 0:
            temp_home_district = choice(district_population)
        else:
            temp_home_district = "NIE WROCLAW"

        if choice(out_of_city) == 0:
            temp_work_district = choice(district_population)
        else:
            temp_work_district = "NIE WROCLAW"

        if choice(out_of_city) == 0:
            temp_fun_district = choice(district_population)
        else:
            temp_fun_district = "NIE WROCLAW"

        temp_age = choice(age)
        # temp_person = f"{temp_name} {temp_surname} wiek:  {temp_age} plec:  {gender} dom: {temp_home_district} praca {temp_work_district} rozrywka {temp_fun_district}"
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
