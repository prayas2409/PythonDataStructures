from Utility.UtilityDataStructures import UtilityDataStructures
flag: bool = True
while flag:
    try:
        print('Enter the number of elements to be added to the array')
        util = UtilityDataStructures()
        num = util.get_positive_integer()
        counter = 0
        array = []
        print("Enter the elements for the array")
        while counter in range(0, num):
            n = util.get_integer()
            array.append(n)
            counter += 1
        for counter in range(0, num):
            print(array[counter], " ")
        print("Enter the number to search and delete")
        search = util.get_integer()
        try:
            array.remove(search)
            num -= 1
            print("After deleting the element in the array")
            for counter2 in range(0, num):
                print(array[counter2], " ")
        except:
            print("Number not found in the array")

    except Exception as e:
        print("Process stopped because %s" % e)
    print("Enter 0 to exit another value to continue")
    if util.get_integer() == 0:
            flag = False
