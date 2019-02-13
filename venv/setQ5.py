from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        set1 = {1, 2, 3, 14, 15}
        print(set1)
        if 16 in set1:
            set1.remove(16)
            print("successfully deleted")
        else:
            print("Not present in the set")
        print(set1)

    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False

