import json

def readJsonFile(FileName):
    data = ""
    try:
        with open(FileName) as json_file:
            data = json.load(json_file)
        return data
    except IOError:
        print("Could not read file")
    return data