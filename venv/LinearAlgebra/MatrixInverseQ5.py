from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        matrix1 = [[3, 1, -1], [2, -2, 0], [1, 2, -1]]

        matrix_object = Matrix()

        adjoint_matrix = [[0, 0, 0]] * 3
        # adjoint_matrix.clear()

        for row in range(0, len(matrix1[0])):
            for col in range(0, len(matrix1)):

                adjoint_matrix[row][col] =item


    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
