from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    s = {1,2,3,14,15}
    print(s)
    if s.__contains__(14):
        s.remove(14)
        print("successfully deleted")
    else:
        print("Not present in the set")
    print(s)
except Exception as e:
    print("Process stopped because %s" % e)
