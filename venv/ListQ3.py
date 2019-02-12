from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = [1,2,3,4,-1,5]
    print("Smallest element is ", min(l1))

except Exception as e:
    print("Process stopped because %s" % e)
