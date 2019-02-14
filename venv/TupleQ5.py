from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        tuple1 = ('apple', 1.23, 54.343, 'f', [10, 20], {20}, 'apple')
        tuple2 = []
        count = 0
        for counter in range(tuple1.__len__()):
            count = 0
            for j in range(counter+1, tuple1.__len__()):
                # tuple 2 will store  the values if it is duplicated in the tuple1 and  was not in tuple2
                if tuple1[counter] == tuple1[j] and (tuple2.__contains__(tuple1[j])) is False:
                    tuple2.append(tuple1[j])
        print(" the elements having the duplicates are ", tuple2)

    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False

