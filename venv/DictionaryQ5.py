
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        dict1 = {'', ''}
        dict1.clear()
        print("Enter the number")
        inputnum = util.get_positive_integer()+1
        dict1 = {(i, i*i) for i in range(1, inputnum)}
        print(dict1)

    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
