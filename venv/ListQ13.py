from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = ['Red', 'yop', 'der', 'poy', 'op', 'edr']
    print("l1 is ", l1)
    l2 = ['pop', 'poy', 'Red']
    print('l2 is ', l2)
    for string in l2:
        l1.append(string)
    print("l1 is ", l1)

except IndexError:
    print(l1)
except Exception as e:
    print("Process stopped because %s" % e)
