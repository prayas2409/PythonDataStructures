'''
Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
'''
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
except:
    print("error")
