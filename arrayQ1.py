'''
Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
'''
import array as ar
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        array1 = ar.array('i',  [1, 2, 3, 4])
        # printing elements in the array
        for counter in array1:
            print(counter)

    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
