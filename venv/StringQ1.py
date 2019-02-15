from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    
    try:
        string1 = "apgdfghdghdffsdfsfsfshdfgffsdfsfsdfsfsdfsfhdfhdfghfhgple"
        # printing the value of the string and the length of the string
        print("String is ", string1, "length of the string is", len(string1))
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
