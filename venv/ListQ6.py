from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = [2, 5, 1, 2, 4, 4, 2, 3, 2, 1]
    l2 = []
    print(l1)
    for i in l1:
        if l2.__contains__(i):
            continue
        else:
            l2.append(i)
    print("Using  diff list ",l2)
    '''
    for i in range (l1.__len__()-1 ):
        for j in range (i+1 , l1.__len__()-1):
            if l1[i] == l1[j]:
                l1 = u.swipeFromRtoL(l1, j, l1.__len__())
                l1.remove(l1[j])
    print("singly ",l1)
    '''
except Exception as e:
    print("Process stopped because %s" % e)
