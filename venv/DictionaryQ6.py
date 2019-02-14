
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:

        dictnew = {'': ''}
        dict1 = {0: 11, 1: 13}
        dict2 = {2: 12, 3: 16}
        dict3 = {4: 14, 5: 17}
        dictnew.clear()
        # storing the elements in the dictionary
        dictnew = dict1.copy()
        dictnew.update(dict2)
        dictnew.update(dict3)
        print("printing as items")
        for items in dictnew.items():
            print(items)

        print("Enter the key to be deleted")
        num = util.get_integer()
        # deleting the element from the dictionary
        try:
            dictnew.__delitem__(num)
            print(dictnew)
        except:
            print('Key not found')

    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
