from src.generator import generate_people, generate_peoples_journeys, count_journeys
from collections import Counter

print("Generowanie osób")

people_number = 1200

people = generate_people(people_number)
generate_peoples_journeys(people)
full = count_journeys(people)
nie_wroclaw = list(filter(lambda person: person['dom'] == 'NIE WROCLAW', people))
# for e in nie_wroclaw:
#     print(e)
