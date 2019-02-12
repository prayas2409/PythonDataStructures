from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    s = {1,2,3,12,13,14}
    print(s)
    s.remove(12)
    print(s)

except Exception as e:
    print("Process stopped because %s" % e)
