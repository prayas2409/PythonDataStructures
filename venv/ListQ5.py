
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        print(list1)
        # sorting the variables according to the second element in each tuple of list
        for i in range(0, list1.__len__()-1):
            for j in range(i+1, list1.__len__()):
                if list1[i][1] > list1[j][1]:
                    temp = list1[i]
                    list1[i] = list1[j]
                    list1[j] = temp

        print(list1)
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
