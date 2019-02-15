from copy import deepcopy
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        tuple1 = tuple(['apple', 1.23, 54.343, 'f', [10, 20], {20}])
        # copying the tuple to different tuple
        tuple2 = deepcopy(tuple1)
        print(tuple1)
        print(tuple2)

    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
