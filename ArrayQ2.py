from Utility.UtilityDataStructures import UtilityDataStructures

try:
    print('Enter the number of elements to be added to the array')
    u = UtilityDataStructures()
    num = u.getPositiveInteger()
    i = 0
    array = []
    print("Enter the elements for the array")
    while(i in range(num)):
        n = u.getInteger()
        array.append(n)
        i += 1
    for i in range(num):
        print(array[i])

    print("After using inbuilt function")
    array.reverse()
    for i in range(num):
        print(array[i])
except Exception as e:
    print("Process stopped because %s" % e)
