from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    s1 = {1,2,3,14,15}
    print(s1)
    s2 = {4,5,6,1,2}
    print(s2)
    s3 = s1 - s2
    print (s3)

except Exception as e:
    print("Process stopped because %s" % e)
