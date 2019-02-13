import itertools
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        list1 = ['Red', 'yop', 'der', 'poy', 'op', 'edr']
        for counter in range(list1.__len__()):
            list1[counter] = list1[counter].lower()
        print(list1)
        charperms = []
        listperms = []
        num = list1.__len__()
        for item in range(list1.__len__()):
            charperms = ['']
            charperms = itertools.permutations(list1[item])
            listperms.clear()
            for each in charperms:
                listperms.append(''.join(each))
            for others in list1[item + 1:]:
                if listperms.__contains__(others):
                    list1.remove(others)
        for counter in range(list1.__len__()):
            print(list1[counter])
    except IndexError:
        print(list1)
    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
