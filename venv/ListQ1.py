
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        l1 = [1, 2, 3, 4, 5]
        print(l1)
        total = 0
        for elements in l1:
            total += elements
        print(total)
        print("also by sum method", sum(l1))
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
