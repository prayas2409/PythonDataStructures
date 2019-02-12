from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(l1)
    for i in range(l1.__len__()-1):
        for j in range(i+1,l1.__len__()):
            if l1[i][1] > l1[j][1]:
                temp = l1[i]
                l1[i] = l1[j]
                l1[j] = temp

    print(l1)

except Exception as e:
    print("Process stopped because %s" % e)
