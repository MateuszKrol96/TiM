import numpy as np
from matplotlib import pyplot as plt

from src.generator import generate_people, generate_peoples_journeys, count_journeys, generate_peoples_opinions
from src import data_districts_parkings, data_corpos

from src.stats import count_sex, count_age_brackets, count_parking_occupation, draw_sum_corpo_car_parks, \
    draw_car_parks_occupation, draw_sex_chart, draw_opinion_age_chart, draw_opinion_district_chart


def absolute_value(val):
    a = np.round(val / 100. * sum(sizes), 0)
    return a


people_number = 100000

people = generate_people(people_number)
generate_peoples_journeys(people)
full = count_journeys(people)
###########################################
###########################################
labels = []
sizes = []

for x, y in full['praca'].items():
    labels.append(x)
    sizes.append(y)

# Plot
plt.figure(figsize=(25, 25))
plt.pie(sizes, labels=labels, autopct=absolute_value)
plt.title("Podroze do pracy", loc="left")

plt.axis('equal')
# plt.show()
###########################################
###########################################
labels = []
sizes = []

for x, y in full['rozrywka'].items():
    labels.append(x)
    sizes.append(y)

# Plot
plt.figure(figsize=(25, 25))
plt.pie(sizes, labels=labels, autopct=absolute_value)
plt.title("Podroze - rozrywka", loc="left")

plt.axis('equal')
# plt.show()
###########################################
###########################################

###########################################
###########################################
list_cap_parks = data_districts_parkings.DISTRICTS_CAR_PARKING
labels = []
sizes = []

for x, y in list_cap_parks.items():
    labels.append(x)
    sizes.append(y)

# Plot
plt.figure(figsize=(25, 25))
plt.pie(sizes, labels=labels, autopct=absolute_value)
plt.title("Dostepne miejsca parkingowe", loc="left")
plt.axis('equal')
# plt.show()
###########################################
###########################################


list_cap_parks = data_districts_parkings.DISTRICTS_CAR_PARKING
parking_occupation = count_parking_occupation(full, list_cap_parks)
people_with_opinions = generate_peoples_opinions(people, parking_occupation)
list_corpo_car_park = data_corpos.CORPOS_CAR_PARKING

sex_stats = count_sex(people)
draw_sex_chart(sex_stats)
age_brackets = count_age_brackets(people)
draw_sex_chart(age_brackets)
draw_opinion_district_chart(people_with_opinions)
draw_opinion_age_chart(people_with_opinions)
#
#
draw_car_parks_occupation(full, list_cap_parks)
draw_sum_corpo_car_parks(list_corpo_car_park)
