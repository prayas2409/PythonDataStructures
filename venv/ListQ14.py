from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = ['10', '10', '100', '0', '0']
    print("l1 is ", l1)
    l2 = ['100', '0', '0', '10', '10']
    print('l2 is ', l2)
    ltemp = ['']
    l1store = []

    if l1.__len__() != l2.__len__():
        print(False)
        exit()
    n = l1.__len__()
    l1 *= 2
    str1 = ''.join(l1)
    print('str1 is', str1)
    str2 = ''.join(l2)
    print('str2 is ', str2)
    if str1.__contains__(str2):
        print(True)
    else:
        print(False)

except IndexError:
    print('in index error ', l1store)
except Exception as e:
    print("Process stopped because %s" % e)
