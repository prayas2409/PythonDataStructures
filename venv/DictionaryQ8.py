
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        # creating a dummy dictionary
        dict1 = {'': ''}
        print(dict1)
        string = 'w3resource'
        dict1.clear()
        # storing the values in the dictionary along with their count
        for i in string:
            dict1[i] = string.count(i)
        print(dict1)
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
