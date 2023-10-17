myFruitList = ["apple", "banana", "cherry"]

print("")
print("######################################### LIST #########################################")
print("")
print(myFruitList)
print(type(myFruitList))

print("0:", myFruitList[0])
print("1:",myFruitList[1])
print("2:",myFruitList[2])
print("-1:",myFruitList[-1])
print("-2:",myFruitList[-2])
print("-3:",myFruitList[-3])

# The tuple is like a list, but it can't be changed. A data type that can't be changed after it's created is said to be immutable.
# To define a tuple, you use parentheses instead of brackets ().

myFinalAnswerTuple = ("apple", "banana", "pineapple")

print("")
print("######################################### TUPLE #########################################")
print("")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


# A dictionary is a list with named positions (keys). Imagine that your list shows people’s favorite fruit.

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print("")
print("######################################### DICTIONARY #########################################")
print("")
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# You will use the name of the individuals to get their favorite fruit, instead of numbers

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
