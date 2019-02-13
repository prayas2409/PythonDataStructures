from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        list1 = ['10', '10', '100', '0', '0']
        print("l1 is ", list1)
        list2 = ['100', '0', '0', '10', '10']
        print('l2 is ', list2)
        listtemp = ['']
        list1store = []

        if list1.__len__() != list2.__len__():
            print(False)
            exit()
        n = list1.__len__()
        list1 *= 2
        str1 = ''.join(list1)
        print('str1 is', str1)
        str2 = ''.join(list2)
        print('str2 is ', str2)
        if str1.__contains__(str2):
            print(True)
        else:
            print(False)

    except IndexError:
        print('in index error ', list1store)
    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
