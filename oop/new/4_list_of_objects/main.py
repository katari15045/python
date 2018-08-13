class Animal:
    name = ""
    horn = True

animals = []

a_1 = Animal()
a_1.name = "Deer"
a_1.horn = True
animals.append(a_1)

a_2 = Animal()
a_2.name="dog"
a_2.horn=False
animals.append(a_2)

print(animals[0].name)
print(animals[1].name)

