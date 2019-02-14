from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        util = UtilityDataStructures()
        tuple1 = tuple(['apple', 'dhoni', 'veejay', 'deepak', 'suhas'])
        print(tuple1)
        print("Enter the item to be removed")
        user_input = input()
        # as tuple is immutable storing the values of tuple in the list
        list1 = list(tuple1)
        # removing the element from the list
        list1.remove(user_input)
        # storing values back to the tuple from the updated list
        tuple1 = tuple(list1)
        print(tuple1)

    except Exception as exep:
        print("Process stopped because %s" % exep)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
