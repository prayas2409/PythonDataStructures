from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = ['abc', 'xyz', 'aba', '1221']
    print(l1)
    l2 = [a for a in l1 if a[0]==a[-1]]
    print(l2)

except Exception as e:
    print("Process stopped because %s" % e)
