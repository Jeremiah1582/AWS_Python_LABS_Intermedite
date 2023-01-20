
import json


def readJsonFile(filename):
    data= ""
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
    except IOError:
        print("could not retrieve the file")
    return data
