from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    dict = {'',''}
    dict1 = {0:11,1:13}
    dict2 = {2:12,3:16,}
    dict3 = {4:14,5:17}
    dict.clear()

    dict = dict1.copy()
    dict.update(dict2)
    dict.update(dict3)
    print("printing as items")
    for items in dict.items():
        print(items)

    print("Enter the key to be deleted")
    num = u.getInteger()

    try:
        dict.__delitem__(num)
        print(dict)
    except:
        print('Key not found')


except Exception as e:
    print("Process stopped because %s" % e)
