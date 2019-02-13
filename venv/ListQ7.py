from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = [2, 5, 1, 2, 4, 4, 2, 3, 2, 1]
    l2 = []
    l2 = l1.copy()
    print(l1)
    print(l2)
except Exception as e:
    print("Process stopped because %s" % e)
