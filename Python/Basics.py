name="Batman"               #input("Name: ")
print(f"Hello, {name}") # get C like formatted printing

n =20            #int(input("Number: "))  # removes type mismatch
if n > 0 :
    print(f"{n} is a positive number")
elif n <0:
    print(f" {n} is a negative number")
else:
    print("n == 0")



fixedName = "Harry"     
print(fixedName[0])     #Strings

#tuples
coordinates = (10.0,20.0)

# Lists

names= ["batman","Lewis","Clark"]
names.append("Bhavya")
names.sort()

# sets

s = set()

s.add(3)
s.add(1)
s.add(2)
s.add(4)
print(s)

print(len(s))

#   loops

for i in [1,2,3,4,5,6,7]:
    print(i,end=" ")

for i in fixedName:
    print(i)

#dictionaries

houses = {"Harry":"Gryffindor","Draco":"Slytherin","Ron":"Gryffindor"}
print(houses["Harry"])
houses["Hermione"] = "Gryffindor"

#functions
def square(x):
    return x*x
print(square(5))
