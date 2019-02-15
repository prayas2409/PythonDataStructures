from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        tuple1 = ('apple', 'dhoni', 'veejay', 'deepak', 'suhas')
        print(tuple1)
        user_input = input("Enter the element to be searched in the tuple")
        # it checks if the user input is present in the tuple
        if tuple1.__contains__(user_input):
            print("the string is present")
        else:
            print("String not present")
    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False

