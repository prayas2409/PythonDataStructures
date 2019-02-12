from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    s = {1,2,3}

    for i in s:
        print(i)

except Exception as e:
    print("Process stopped because %s" % e)
