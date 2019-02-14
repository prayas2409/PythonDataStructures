
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:

        matrix1 = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
        print(matrix1)
        matrix2 = [5, 8, 1]
        print(matrix2)
        matrix3 = [[]]
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
