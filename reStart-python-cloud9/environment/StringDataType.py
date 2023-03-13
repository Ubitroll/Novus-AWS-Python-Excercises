myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print()
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print()
name = input("What is your name?")
print(name)
print()
colour = input("What is your favourite colour?")
animal = input("What is your favourite animal?")
print("{}, you like a {} {}!".format(name,colour,animal))