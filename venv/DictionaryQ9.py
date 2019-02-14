
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        dict1 = {'1': 1}
        string = 'w3resource'
        dict1.clear()
        for i in string:
            dict1[i] = string.count(i)
            # printing the key and values as tables
        for (key, vals) in dict1.items():
            print(key, " \t", vals)
    except Exception as e:
            print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
