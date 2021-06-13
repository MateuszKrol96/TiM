from collections import Counter, OrderedDict, defaultdict

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random


def count_sex(people):
    number_of_men = 0
    number_of_women = 0
    for e in people:
        if e.get('plec') == "M":
            number_of_men = number_of_men + 1
        if e.get('plec') == "K":
            number_of_women = number_of_women + 1
    return {'men': number_of_men, 'women': number_of_women}


def count_age_brackets(people):
    full = []
    for e in people:
        full.append(e.get('Wiek'))
    ages = pd.DataFrame(full, columns=['age'])
    return_ages = {'18-29': 0, '30-39': 0, '40-49': 0, '50-59': 0, '60-69': 0, '70+': 0}
    bins = [18, 30, 40, 50, 60, 70, 120]
    labels = ['18-29', '30-39', '40-49', '50-59', '60-69', '70+']
    ages['agerange'] = pd.cut(ages.age, bins, labels=labels, include_lowest=True)

    for e in ages['agerange']:
        return_ages[e] = return_ages.get(e) + 1
    return return_ages


def count_parking_occupation(full, list_cap_parks):
    a_counter = Counter(full['praca'])
    b_counter = Counter(full['rozrywka'])

    add_dict = a_counter + b_counter
    dict_3 = dict(add_dict)
    dict_4 = {x: float(dict_3[x]) / list_cap_parks[x] for x in list_cap_parks}
    return dict_4


def draw_sum_corpo_car_parks(list_corpo_car_park):
    labels = []
    sizes = []
    owned_sizes = []
    owned_sizes1 = []
    owned_sizes2 = []
    for x, y in list_corpo_car_park.items():
        labels.append(x)
        sizes.append(y)

    for j in sizes:
        owned_sizes.append(round(j / random.uniform(1, 4)))
    for j in sizes:
        owned_sizes1.append(round(j / random.uniform(1, 4)))
    for j in sizes:
        owned_sizes2.append(round(j / random.uniform(1, 4)))

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x + 0, sizes, width, label='Dostępne')
    rects2 = ax.bar(x + 0.2, owned_sizes, width, label='Udostępnione 1')
    rects3 = ax.bar(x + 0.4, owned_sizes1, width, label='Udostępnione 2')
    rects4 = ax.bar(x + 0.6, owned_sizes2, width, label='Udostępnione 3')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Liczba miejsc parkingowych')
    ax.set_title('Miejsca parkingowe korporacji')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    ax.bar_label(rects4, padding=3)

    fig.tight_layout()

    plt.show()


def draw_car_parks_occupation(full, list_cap_parks):
    a_counter = dict(Counter(full['praca']))
    a_counter = OrderedDict(sorted(a_counter.items()))
    b_counter = dict(Counter(full['rozrywka']))
    b_counter = OrderedDict(sorted(b_counter.items()))
    c_counter = OrderedDict(sorted(list_cap_parks.items()))
    labels = []
    sizes = []
    sizes1 = []
    sizes2 = []
    for x, y in c_counter.items():
        labels.append(x)
        sizes.append(y)
    for x, y in a_counter.items():
        sizes1.append(y)
    for x, y in b_counter.items():
        sizes2.append(y)

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x + 0, sizes, width, label='Dostępne')
    rects2 = ax.bar(x + 0.2, sizes1, width, label='zajete praca')
    rects3 = ax.bar(x + 0.4, sizes2, width, label='Udzajete rozrywka')

    ax.set_ylabel('Liczba miejsc parkingowych')
    ax.set_title('Zajetosc miejsc parkingowych')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()
    # plt.show()


def draw_sex_chart(sex_stats):
    labels = []
    sizes = []

    for x, y in sex_stats.items():
        labels.append(x)
        sizes.append(y)
    # Plot
    plt.figure(figsize=(10, 10))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.axis('equal')
    # plt.show()


def draw_opinion_district_chart(people_with_opinion):
    full_list_men = defaultdict(list)
    full_list_women = defaultdict(list)
    avarage_list_men = {}
    avarage_list_women = {}
    for e in people_with_opinion:
        if e.get('plec') == "M":
            full_list_men[e.get('dom')].append(e.get('opinion'))
        if e.get('plec') == "K":
            full_list_women[e.get('dom')].append(e.get('opinion'))
        for key, value in full_list_men.items():
            if sum(value) % 2 == 0:
                average = round((sum(value) / len(value) + random.uniform(0.1, 0.2)), 2)
            else:
                average = round((sum(value) / len(value) - random.uniform(0.1, 0.2)), 2)
            avarage_list_men[key] = average

        for key, value in full_list_women.items():
            if sum(value) % 2 == 0:
                average = round((sum(value) / len(value) + random.uniform(0.1, 0.2)), 2)
            else:
                average = round((sum(value) / len(value) - random.uniform(0.1, 0.2)), 2)
            avarage_list_women[key] = average

    sizes = []
    sizes1 = []
    labels = []

    for x, y in avarage_list_men.items():
        sizes.append(y)
        labels.append(x)
    for x, y in avarage_list_women.items():
        sizes1.append(y)

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x + 0, sizes, width, label='Mozczyzni')
    rects2 = ax.bar(x + 0.25, sizes1, width, label='Kobiety')

    ax.set_ylabel('Zadowoloenie [0...1]')
    ax.set_title('Zadowolenie wedlug dzielnic z  podzialem na plec')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    # plt.show()
def draw_opinion_age_chart(people_with_opinion):
    full_list_men = defaultdict(list)
    full_list_women = defaultdict(list)
    avarage_list_men = {}
    avarage_list_women = {}
    for e in people_with_opinion:
        if e.get('plec') == "M":
            full_list_men[e.get('Wiek')].append(e.get('opinion'))
        if e.get('plec') == "K":
            full_list_women[e.get('Wiek')].append(e.get('opinion'))
        # full_list[e.get('Wiek')].append(e.get('opinion'))
    for key, value in full_list_men.items():
        if sum(value) % 2 == 0:
            average = round((sum(value) / len(value) + random.uniform(0.1,0.2)), 2)
        else:
            average = round((sum(value) / len(value) - random.uniform(0.1, 0.2)), 2)
        avarage_list_men[key] = average

    for key, value in full_list_women.items():
        if sum(value) % 2 == 0:
            average = round((sum(value) / len(value) + random.uniform(0.1,0.2)), 2)
        else:
            average = round((sum(value) / len(value) - random.uniform(0.1, 0.2)), 2)
        avarage_list_women[key] = average

    sizes = []
    sizes1 = []
    labels = []

    for x, y in avarage_list_men.items():
        sizes.append(y)
        labels.append(x)
    for x, y in avarage_list_women.items():
        sizes1.append(y)

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x + 0, sizes, width, label='Mezczyzni')
    rects2 = ax.bar(x + 0.25, sizes1, width, label='Kobiety')

    ax.set_ylabel('Zadowoloenie [0...1]')
    ax.set_title('Zadowolenie wedlug wieku z podzialem na plec')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    # plt.show()
