from Utility.UtilityDataStructures import UtilityDataStructures

try:
    print('Enter the number of elements to be added to the array')
    u = UtilityDataStructures()
    num = u.getPositiveInteger()
    i = 0
    array = []
    print("Enter the elements for the array")
    count = 0
    while i in range(num):
        n = u.getInteger()
        array.append(n)
        i += 1

    print("Enter the number to be searched")
    search = u.getInteger()
    for i in range(num):
        if array[i].__eq__(search):
            count += 1
    print("The number of occurrences  of ",search," are ",count)
except Exception as e:
    print("Process stopped because %s" % e)
