import pprint

from matplotlib import pyplot as plt

from main import absolute_value
from src import data_districts_parkings
from src.generator import generate_people, generate_peoples_journeys, count_journeys
from collections import Counter

print("Generowanie osób")

people_number = 1200

list_cap_parks = data_districts_parkings.DISTRICTS_CAR_PARKING
labels = []
sizes = []

for x, y in list_cap_parks.items():
    labels.append(x)
    sizes.append(y)
# Plot
plt.figure(figsize=(25, 25))
plt.pie(sizes, labels=labels, autopct=absolute_value)

plt.axis('equal')
plt.show()
