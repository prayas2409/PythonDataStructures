
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        string1 = input("Enter the text to reverse")
        print(string1)
        # joining the result provided by reversed function as it'll return multiple objects
        string2 = "".join(reversed(string1))
        print(string2)
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
