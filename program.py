import random

import numpy as np
from matplotlib import pyplot as plt

from src import data_districts_parkings, data_corpos
from src.generator import generate_people, generate_peoples_journeys, count_journeys
from collections import Counter

def absolute_value(val):
    a = np.round(val / 100. * sum(sizes), 0)
    return a


print("Generowanie Miejsc parkingowych")

people_number = 1200

list_cap_parks = data_districts_parkings.DISTRICTS_CAR_PARKING
labels = []
sizes = []

for x, y in list_cap_parks.items():
    labels.append(x)
    sizes.append(y)

# Plot
plt.figure(figsize=(25, 25))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Zliczone miejsca parkingowe", loc="left")

plt.axis('equal')
plt.show()

list_corpo_car_park = data_corpos.CORPOS_CAR_PARKING
labels = []
sizes = []

for x, y in list_corpo_car_park.items():
    labels.append(x)
    sizes.append(y)
# Plot
plt.figure(figsize=(25, 25))
plt.pie(sizes, labels=labels, autopct=absolute_value)

plt.axis('equal')
plt.show()
