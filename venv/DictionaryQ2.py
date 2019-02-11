import string

from Utility.UtilityDataStructures import UtilityDataStructures
u = UtilityDataStructures()
try:
    dict = {"0":11,"1":13,"2":12,"3":16,'4':14}
    print("The dictionary before sorting is")
    for key in dict:
        print("For key ",key, " value is: ",dict[key])

    keys = [key for key in dict]
    values = [dict[key] for key in dict]
    temp = 0
    j = 0
    print("Enter the key to be added")
    inkey = u.getInteger()
    print("Enter the value to be added")
    invalue = u.getInteger()

    print("the dict after manipulation with key")
    dict[inkey.__str__()] = invalue
    print(dict)
except Exception as e:
    print("Process stopped because %s" % e)
