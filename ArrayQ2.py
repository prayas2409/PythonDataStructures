from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        print('Enter the number of elements to be added to the array')
        util = UtilityDataStructures()
        num = util.get_positive_integer()
        counter = 0
        array = []
        print("Enter the elements for the array")
        while counter in range(num):
            inputnum = util.get_integer()
            array.append(inputnum)
            counter += 1
        for counter in range(num):
            print(array[counter])

        print("After using inbuilt reverse function")
        array.reverse()
        for counter in range(num):
            print(array[counter])

    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
