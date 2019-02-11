from Utility.UtilityDataStructures import UtilityDataStructures
u = UtilityDataStructures()
try:
    dict = {'',''}
    dict1 = {0:11,1:13}
    dict2 = {2:12,3:16,}
    dict3 = {4:14,5:17}
    print("The dictionary before sorting is")

    print("The 3 dictionaries are")
    print(dict1)
    print(dict2)
    print(dict3)
    print("Testing")

    dict.clear()

    dict = dict1.copy()
    dict.update(dict2)
    dict.update(dict3)


    print("the resultant dict is")
    print(dict)

    for key in dict:
        print ("key: ",key," value: ",dict[key])

except Exception as e:
    print("Process stopped because %s" % e)
