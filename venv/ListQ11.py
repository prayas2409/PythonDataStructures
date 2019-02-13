from Utility.UtilityDataStructures import UtilityDataStructures
from itertools import permutations

u = UtilityDataStructures()
iter
try:
    l1 = ['Red', 'yop', 'der', 'poy', 'op', 'edr']
    for i in range (l1.__len__()):
        l1[i] = l1[i].lower()
    print(l1)
    lperms = []
    listperms = []
    num = l1.__len__()
    for it in range(l1.__len__()):
        lperms = ['']
        lperms = permutations(l1[it])
        listperms.clear()
        for each in lperms:
            listperms.append(''.join(each))
        for others in l1[it+1:]:
            if listperms.__contains__(others):
                l1.remove(others)
    for i in range(l1.__len__()):
        print(l1[i])
except IndexError:
    print(l1)
except Exception as e:
    print("Process stopped because %s" % e)
