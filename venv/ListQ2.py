from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = [1,2,3,4,5]
    print(l1)
    total = 1
    for i in l1:
        total *= i
    print (total)
except Exception as e:
    print("Process stopped because %s" % e)
