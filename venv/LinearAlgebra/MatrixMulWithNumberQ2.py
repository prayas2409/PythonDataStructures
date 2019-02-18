
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:

        matrix1 = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

        print(matrix1)
        print("Enter a number to multiply with the matrix")
        num_input = util.get_integer()
        # multiplying the elements with single number the elements at the same positions
        matrix3 = [[matrix1[row][col] * num_input for row in range(0, 3)] for col in range(0, 3)]
        print(matrix3)
    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if input() == 0:
        flag = False
