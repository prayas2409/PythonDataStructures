from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        matrix1 = [[1, 2, 3], [3, 4, 5], [7, 6, 4]] 
        print(matrix1)
        matrix2 = [[5, 2, 6], [5, 6, 7], [7, 6, 4]]
        print(matrix2)
        matrix3 = [[0 for row in range(3)] for col in range(3)]

        # matrix3 = [[[matrix3[row][col] += matrix1[row][col] * matrix2[row][col]] for row in range(0, 3)] for col in range(0, 3)]

        for row in range(0, matrix1[0].__len__()):
            for col in range(0, len(matrix2)):
                for count in range(0, matrix2[0].__len__()):
                    matrix3[row][col] += matrix1[row][count] * matrix2[count][col]

        print(matrix3)
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
