from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        list1 = ['Red', 'yop', 'der', 'poy', 'op', 'edr']
        print("l1 is ", list1)
        list2 = ['pop', 'poy', 'Red']
        print('l2 is ', list2)
        list3 = []
        for string1 in list1:
            if list2.__contains__(string1):
                continue
            else:
                list3.append(string1)

        print('l3 is ', list3)
    except IndexError:
        print(list1)
    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
