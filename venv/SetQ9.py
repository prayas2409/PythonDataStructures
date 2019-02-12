from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    s1 = {1,2,3,14,15}
    print(s1)
    s1.clear()
    print (s1)

except Exception as e:
    print("Process stopped because %s" % e)
