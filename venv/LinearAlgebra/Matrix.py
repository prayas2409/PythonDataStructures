class Matrix:

    def __set__(self, matrix_passed):
        self.matrix_original = matrix_passed

    def __get__(self):
        return self.matrix_original

    def print_Matrix(self, matrix_passed):
        print("printing the matrix")
        for item in matrix_passed:
            print(item)

    def cofactors(self, row, col, matrix_passed):
        list1 = list()
        for row1 in range(0, len(matrix_passed[row])):
            for col1 in range(0, len(matrix_passed[row])):
                if row1 != row and col1 != col:
                    list1.append(matrix_passed[row1][col1])
        counter = 0
        item = (list1[counter] * list1[-(counter + 1)])
        counter += 1
        item = item - (list1[counter] * list1[-(counter + 1)])
        print(" item is ", item)
        return item

    def transpose_Matrix(self, matrix_passed):
        print("Creating transpose for a matrix")
        transpose_adj_matrix = [[matrix_passed[row][col] for row in range(0, len(matrix_passed[0]))] for col in range(0, len(matrix_passed))]
        return transpose_adj_matrix

    def calculate_adjoint(self, matrix_passed):
        adjoint_matrix = []

        for row in range(0, len(matrix_passed[0])):
            list1 = list()
            for col in range(0, len(matrix_passed)):
                item = self.cofactors(row, col, matrix_passed)
                list1.append(item)
            adjoint_matrix.append(list1)
        
        return adjoint_matrix

    def calculate_determinant(self, matrix_passed):
        temp = -1
        item = 0
        for col in range(0, len(matrix_passed)):
            cofactor = self.cofactors(0, col, matrix_passed)

            item += (temp*-1) * (matrix_passed[0][col] * cofactor)
        return item

    def matrix_multiply(self, matrix1, matrix2):
        matrix3 = [[0, 0, 0]] * 3

        for row in range(0, matrix1[0].__len__()):
            for col in range(0, len(matrix2)):
                for count in range(0, matrix2[0].__len__()):
                    matrix3[row][col] += matrix1[row][count] * matrix2[count][col]
        print("The multiplication is")
        self.print_Matrix(matrix3)

    def inverse_Matrix(self,):
        matrix1 = [[1, 3, 7], [4, 2, 3], [1, 2, 1]]
        self.print_Matrix(matrix1)
        adjoint_matrix = self.calculate_adjoint(matrix1)
        self.print_Matrix(adjoint_matrix)
        adjoint_matrix = self.transpose_Matrix(adjoint_matrix)
        self.print_Matrix(adjoint_matrix)
        determinant = self.calculate_determinant(matrix1)
        print(determinant)
        inverse_matrix = [[adjoint_matrix[row][col]/determinant for col in range(0, len(matrix1[row]))] for row in range(0, len(matrix1))]
        print("or \n 1/", determinant, 'x')
        self.print_Matrix(adjoint_matrix)
        print("checking if inverse is right")
        self.matrix_multiply(matrix1, inverse_matrix)


matrix_object = Matrix()
matrix_object.inverse_Matrix()
