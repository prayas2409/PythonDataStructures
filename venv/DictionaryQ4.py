
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        dictnew = {'': ''}
        dict1 = {'0': 11, 1: 13}
        dict2 = {'2': 12, 3: 16}
        dict3 = {'4': 14, 5: 17}
        # clearing the dictionary for storing the new values
        dictnew.clear()
        # updating the dictionary if keys not present then gets added
        dictnew = dict1.copy()
        dictnew.update(dict2)
        dictnew.update(dict3)

        print("printing as items")
        for items in dictnew.items():
            print(items)

        print("printing using keys")
        for k in dictnew:
            print("Key: ", k, " values:", dictnew[k])

        print("printing key value pairs")
        for (k, v) in dictnew.items():
            print("Key: ", k, " values:", v)

    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
