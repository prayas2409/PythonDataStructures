from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        list1 = ['Prayas', 'Deepak', 'Sunil', 'Veejay', 'Suhas', 'Narayan', 'Ajay']
        list2 = ['Rakesh', 'sunil', 'Manoj']
        flag = False
        for string1 in list1:
           for string2 in list2:
               if string1.lower() == string2.lower():
                    print(True)
                    exit()
        print(False)

    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False

