myString = "This is a string."

print(myString)
print(type(myString))
print(myString + " is of the data type: " + str(type(myString)))

# The plus sign (+) is used to concatenate strings.

firstString = "Water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What's your name? ")
print(name)

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

print("{}, you like a {} {}!".format(name,color,animal))