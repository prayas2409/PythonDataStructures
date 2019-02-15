
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:

        matrix1 = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
        print(matrix1)
        matrix2 = [1, 2, 3]
        print(matrix2)
        item = 0
        '''
        matrix3 = [[ [item += (matrix1[row][col] * matrix2[0][col])] for row in range(0, 3)] for col in range(0, 3)]

        for row in range(0, 3):
            for col in range(0, 3):
                item = 0;
                for i in  range(0,3):
                    item +=

    '''

    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
