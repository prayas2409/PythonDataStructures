
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        string1 = "width"
        number = 50
        # formatting the string and then printing it
        print("%s=%d" % (string1, number))
        print("{}={}".format(string1, 40))
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
