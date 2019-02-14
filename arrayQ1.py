'''
Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
'''
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        print('Enter the number of elements to be added to the array')
        # getting an input as a positive integer as the size of the new array can't be
        num = util.get_positive_integer()
        counter = 0
        array = []
        print("Enter the elements for the array")
        # storing the elements in the array
        while counter in range(num):
            inputnum = util.get_integer()
            array.append(inputnum)
            counter += 1
        for counter in range(num):
            print(array[counter])

    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
