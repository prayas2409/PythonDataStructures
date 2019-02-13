from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = ['Red', 'yop', 'der', 'poy', 'op', 'edr']
    print("l1 is ", l1)
    l2 = ['pop', 'poy', 'Red']
    print('l2 is ', l2)
    l3 = []
    for string1 in l1:
        if l2.__contains__(string1):
            continue
        else:
            l3.append(string1)

    print('l3 is ', l3)
except IndexError:
    print(l1)
except Exception as e:
    print("Process stopped because %s" % e)
