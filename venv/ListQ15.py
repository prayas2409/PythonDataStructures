from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = ['Red', 'yop', 'der', 'poy', 'op', 'edr']
    print("l1 is ", l1)
    l2 = ['pop', 'poy', 'Red']
    print('l2 is ', l2)
    l3 = []
    for string in l1:
        if l2.__contains__(string):
            l3.append(string)
    print("Common items in l1 and l2 are ", l3)
except IndexError:
    print(l1)
except Exception as e:
    print("Process stopped because %s" % e)
