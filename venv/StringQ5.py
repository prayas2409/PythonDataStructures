from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        list1 =[]
        num_input = util.get_positive_integer()
        for counter in range(0, num_input):
            list1.append(input("Enter the string"))
        llenght = 0
        for item in list1:
            if item.__len__() > llenght:
                llenght = item.__len__()
        print('')

    except IndexError:
        print(string1)
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
