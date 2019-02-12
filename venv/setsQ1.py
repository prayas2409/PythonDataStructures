from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    s = {1,2,3}
    print(s)

except Exception as e:
    print("Process stopped because %s" % e)
