person = {"name": "Bill", "age": '30'}

print(person.get("address", "Not set"))

print(person.get("name", "Not set"))

address = person.get("address", -1)

name = person.get("name", "Not set")

if address < 0:
    print("Address not set")


print(person.pop("name"))

print(person)

person.update({"name": "Jill"})

print(person)

person["weight"] = 76

print(person)

if not person.get('height'):
    person['height'] = 200

# person['dogs'] : ['Patron']

# dct2 = {"dog":"Patron", }

person.update(dogs = ["Patron"])

# person['dogs'] = 'Patron'

print(person)

# print(person)

# dogs = person['dogs']

# dogs.append('Bobik')

# person['dogs'] = dogs

# print(person)



