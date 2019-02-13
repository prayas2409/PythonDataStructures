
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        list1 = ['abc', 'xyz', 'aba', '1221']
        print(list1)
        list2 = [item for item in list1 if item[0] == item[-1]]
        print(list2)

    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
