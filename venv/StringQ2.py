from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        string1 = "google.com"
        # storing the characters in set as duplicates will be removed
        set1 = set(string1)
        #  checking for all the characters in the set
        for char in set1:
            print("count of ", char, " is", string1.count(char))

    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
