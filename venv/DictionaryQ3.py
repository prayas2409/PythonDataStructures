
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        dictnew = {'', ''}
        dict1 = {0: 11, 1: 13}
        dict2 = {2: 12, 3: 16}
        dict3 = {4: 14, 5: 17}
        print("The dictionary before sorting is")

        print("The 3 dictionaries are")
        print(dict1)
        print(dict2)
        print(dict3)
        print("Testing")

        dictnew.clear()
        dictnew = dict1.copy()
        dictnew.update(dict2)
        dictnew.update(dict3)
        print("the resultant dict is")
        print(dictnew)

        for key in dictnew:
            print("key: ", key, " value: ", dictnew[key])

    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
