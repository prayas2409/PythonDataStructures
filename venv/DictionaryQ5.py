from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    dict = {'',''}
    dict.clear()
    print("Enter the number")
    num = u.getPositiveInteger()+1
    dict = { (i,i*i) for i in range(1,num) }
    print (dict)

except Exception as e:
    print("Process stopped because %s" % e)
