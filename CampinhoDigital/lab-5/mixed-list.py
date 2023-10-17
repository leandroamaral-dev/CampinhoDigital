# You can mix data types in a Python list. In other languages, this capability is not a feature of lists.

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))
