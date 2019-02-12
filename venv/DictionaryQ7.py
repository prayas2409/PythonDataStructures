from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    dict = {"IV":"S001", "VII": "S002", "VI": "S001", "IIV": "S005", "IIIV":"S005", "V":"S009","VIII":"S007"}
    print(dict)
    keys = [key for key in dict]
    print(keys)
    values = [v for (k,v) in dict.items()]
    print(values)

    print("Printing the list created by sets")
    llist = set(dict.values())
    for i in llist:
        print(i, " ")
    print("iterating")

except Exception as e:
    print("Process stopped because %s" % e)
