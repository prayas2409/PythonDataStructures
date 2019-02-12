from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = [1,2,3,4,5]
    print(l1)
    total = 0
    for i in l1:
        total += i
    print (total)
    print ("also by sum method",sum(l1))
except Exception as e:
    print("Process stopped because %s" % e)
