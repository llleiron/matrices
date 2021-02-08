# import numpy as np
import random

class matrix:
    def __init__(self, d2_array):
        matrix.__validate__(d2_array)
        self.d2_array = d2_array

    @staticmethod
    def __validate__(array):
        temp = len(array[0])
        for i in range(0, len(array)):
            if not len(array[i]) == temp:
                raise Exception('all raws of giver matrix are not equal')
            temp = len(array[i])
            for j in range(0, len(array[0])):
                if not isinstance(array[i][j], int) or isinstance(array[i][j], float):
                    raise Exception('not all items in matrix are numeric')
     
    def __add__(self, other_matrix):
        if not self.same_dimention_with(other_matrix):
            raise Exception('the dimention of given matrix is another from an instance matrix')
        result = other_matrix
        for i in range(0, len(self.d2_array)):
            for j in range(0, len(self.d2_array[0])):
                result[i][j] = self.d2_array[i][j] + other_matrix[i][j]
        return result
    
    def __sub__(self, other_matrix):
        if not self.same_dimention_with(other_matrix):
            raise Exception('the dimention of given matrix is another from an instance matrix')
        result = other_matrix
        for i in range(0, len(self.d2_array)):
            for j in range(0, len(self.d2_array[0])):
                result[i][j] = self.d2_array[i][j] - other_matrix[i][j]
        return result

    def __mul__(self, other_matrix):
        if not self.same_dimention_with(other_matrix):
            raise Exception('the dimention of given matrix is another from an instance matrix')
        result = other_matrix
        for i in range(0, len(self.d2_array)):
            for j in range(0, len(self.d2_array[0])):
                result[i][j] = self.d2_array[i][j] * other_matrix[i][j]
        return result

    def __tostr__(self, other_matrix):
        result = ''
        for i in range(0, len(other_matrix)):
            result += '[ '
            for j in range(0, len(other_matrix[0])):
                result += f'{other_matrix[i][j]} '
            result += (']\n')
        return result
    

    def determinant(self, total= 0):
        indices = list(range(len(self.d2_array)))
        if len(self.d2_array) == 2 and len(self.d2_array[0]) == 2:
            val = self.d2_array[0][0] * self.d2_array[1][1] - self.d2_array[1][0] * self.d2_array[0][1]
            return val
        
        for fc in indices:
            As = matrix.copy_matrix(self.d2_array)
            As = As[1:]
            height = len(As)

            for i in range(height):
                As[i] = As[i][0:fc] + As[i][fc+1:]
            As = matrix(As)
            sign = (-1) ** (fc % 2)
            sub_det = As.determinant()
            total += sign * self.d2_array[0][fc] * sub_det
        return total

    def inverse(self):
        result = np.linalg.inv(self.d2_array)
        return result

    def  same_dimention_with(self, other_matrix):
        if not len(self.d2_array) == len(other_matrix): 
            return False
        for i in range(0, len(self.d2_array)):
            if not len(self.d2_array[i]) == len(other_matrix[i]):
                return False
        return True

    def issquare(self):
        if len(self.d2_array) == len(self.d2_array[0]):
            return True
        return False
    
    @staticmethod
    def zeros_matrix(rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)

        return M

    @staticmethod
    def copy_matrix(M):
        rows = len(M)
        cols = len(M[0])

        MC = matrix.zeros_matrix(rows, cols)

        for i in range(rows):
            for j in range(cols):
                MC[i][j] = M[i][j]

        return MC

    @staticmethod
    def random_matrix(n, m):
        rand_matrix = matrix([[random.uniform(100, 200) for i in range(n)] for j in range(m)])
        return rand_matrix

if __name__ == '__main__':
    m = matrix([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    print(m.determinant())
