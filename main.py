from src.generator import generate_people, generate_peoples_journeys, count_journeys
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

print("Generowanie osób")


def absolute_value(val):
    a = np.round(val / 100. * sum(sizes), 0)
    return a


people_number = 10000

people = generate_people(people_number)
generate_peoples_journeys(people)
full = count_journeys(people)

# Data to plot
labels = []
sizes = []

for x, y in full['praca'].items():
    labels.append(x)
    sizes.append(y)

# Plot
plt.figure(figsize=(25, 25))
plt.pie(sizes, labels=labels, autopct=absolute_value)

plt.axis('equal')
plt.show()
