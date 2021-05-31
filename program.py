from src.generator import generate_people
from collections import Counter

print("Generowanie osób")

people_number = 1200

people = generate_people(people_number)

nie_wroclaw = list(filter(lambda person: person['dom'] == 'NIE WROCLAW', people))
for e in nie_wroclaw:
    print(e)
