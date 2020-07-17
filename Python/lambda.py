people = [
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Hufflepuff"},
    {"name":"Draco","house":"Slytherine"},
    
]

#def f(person):
   # return person["house"]

people.sort(key=lambda person:person["name"])

print(people)