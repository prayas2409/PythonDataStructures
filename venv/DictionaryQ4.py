from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    dict = {'',''}
    dict1 = {'0':11,1:13}
    dict2 = {'2':12,3:16,}
    dict3 = {'4':14,5:17}
    dict.clear()

    dict = dict1.copy()
    dict.update(dict2)
    dict.update(dict3)
    print("printing as items")
    for items in dict.items():
        print(items)

    print("printing using keys")
    for k in dict:
        print("Key: ",k," values:",dict[k])
    print("printing key value pairs")
    for (k,v) in dict.items():
        print("Key: ", k, " values:", v)

except Exception as e:
    print("Process stopped because %s" % e)
