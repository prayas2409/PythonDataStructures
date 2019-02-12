from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    dict = {'1': 1}
    string = 'w3resource'
    dict.clear()
    for i in string:
        dict[i] = string.count(i)
    print(dict)
except Exception as e:
    print("Process stopped because %s" % e)
