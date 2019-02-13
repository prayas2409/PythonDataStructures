
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        dict1 = {"0": 11, "1": 13, "2": 12, "3": 16, '4': 14}
        print("The dictionary before sorting is")
        for key in dict1:
            print("For key ",key, " value is: ",dict1[key])

        keys = [key for key in dict1]
        values = [dict1[key] for key in dict1]
        temp = 0
        j = 0
        print("Enter the key to be added")
        inputkey = util.get_integer()
        print("Enter the value to be added")
        inputvalue = util.get_integer()

        print("the dict after manipulation with key")
        dict1[inputkey.__str__()] = inputvalue
        print(dict1)
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
