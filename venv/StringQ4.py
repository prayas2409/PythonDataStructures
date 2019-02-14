from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        string1 = input("Enter a string")
        if string1.__len__() < 3:
            print("no change")
        else:
            if string1.endswith("ing"):
                string1 += 'ly'
            else:
                string1 += 'ing'
            print(string1)
    except IndexError:
        print(string1)
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
