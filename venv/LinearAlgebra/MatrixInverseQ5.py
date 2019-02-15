from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        matrix1 = [[1, 2, 3], [3, 4, 5], [7, 6, 4]]
        for item in matrix1:
            print(item)

        

        transpose = [[matrix1[row][col] for row in range(0, len(matrix1[0]))] for col in range(0, len(matrix1))]
        print("The inverse for given matrix is")
        for item in transpose:
            print(item)
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
