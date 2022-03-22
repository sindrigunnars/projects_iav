# Sindri Gunnarsson
# 22-03-22
# Class that handles matrices
def is_numeric(input_number):
    """Checks if an input is numeric"""
    try:
        float(input_number)
        return True
    except TypeError:
        return False


class Matrix:
    def __init__(self, rows=0, cols=0):
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        """Returns a string for the matrix that the print function uses"""
        string = ''
        for i in self.matrix:
            i_str = [str(x) for x in i]
            string += '[ ' + ' '.join(i_str) + ' ]\n'
        return string.strip()

    def __mul__(self, value):
        """Multiplies matrix with number if appropriate,
        otherwise it multiplies two matrices"""
        matrix_mult = Matrix()
        is_number = is_numeric(value)
        try:
            if is_number:
                multiplied = [[i * value for i in j]
                                for j in self.matrix]
            else:
                multiplied = [[0 for _ in self.matrix]
                                for _ in value.matrix[0]]
                for i, _ in enumerate(self.matrix):
                    for j, _ in enumerate(value.matrix[0]):
                        for k, _ in enumerate(value.matrix):
                            multiplied[i][j] += self.matrix[i][k] * value.matrix[k][j]

            matrix_mult.matrix = multiplied
            return matrix_mult
        except IndexError:
            return None

    def __sub__(self, other):
        """Subtracts one matrix from the other if of the same size"""
        sub = Matrix()
        subtracted = [[0 for _ in enumerate(self.matrix[0])]
                      for _ in enumerate(self.matrix)]
        try:
            for i, _ in enumerate(subtracted):
                for j, _ in enumerate(subtracted[0]):
                    subtracted[i][j] = self.matrix[i][j] - other.matrix[i][j]
            sub.matrix = subtracted
            return sub
        except:
            return None

    def __add__(self, other):
        """Adds one matrix to the other if of the same size"""
        add = Matrix()
        addition = [[0 for _ in enumerate(self.matrix[0])]
                    for _ in enumerate(self.matrix)]
        try:
            for i, _ in enumerate(addition):
                for j, _ in enumerate(addition[0]):
                    addition[i][j] = self.matrix[i][j] + other.matrix[i][j]
            add.matrix = addition
            return add
        except:
            return None

    def set_matrix(self, matrix):
        """Sets the values and size of the matrix"""
        self.matrix = [[j for j in i] for i in matrix]

    def set_element(self, rows, cols, value):
        """Changes an element in the matrix based on row and column"""
        self.matrix[rows][cols] = value

    def transpose(self):
        """Transposes the matrix"""
        result = [[0 for _ in enumerate(self.matrix)]
                  for _ in enumerate(self.matrix[0])]
        original = [[i for i in j] for j in self.matrix]
        for i, _ in enumerate(original):
            for j, _ in enumerate(original[0]):
                result[j][i] = original[i][j]
        self.matrix = result


