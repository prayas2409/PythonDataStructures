from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        tuple1 = ('apple', 1.23, 54.343, 'f', [10, 20], {20})
        # storing the values in different variables
        tuple0 = tuple1[0]
        tuple2 = tuple1[1]
        tuple3 = tuple1[2]
        tuple4 = tuple1[5]
        # printing each of the variables taken from tuple
        print(tuple0)
        print(tuple2)
        print(tuple3)
        print(tuple4)

    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False

