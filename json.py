import json

persons = {
    'name': 'Alex',
    'age': 14,

    'name': 'Bob',
    'age': 15,

    'name': 'Mark',
    'age': 13
}

with open('persons.json', 'w') as file:
    for i in range(4):
        json.dump(persons, file, indent=3)
