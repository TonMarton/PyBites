class Matrix:

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other: 'Matrix'):
        new_matrix: list = []
        for i in range(len(self.values)):
            new_part: list = []
            for k in range(len(self.values[0])):
                sum_part: int = 0
                for l  in range(len(self.values[0])):
                    sum_part += self.values[i][l] * other.values[l][k]
                new_part.append(sum_part)
            new_matrix.append(new_part)
        return Matrix(new_matrix)

    def __imatmul__(self, other: 'Matrix'):
        new_matrix = self.__matmul__(other)
        self.values = new_matrix.values
        return self

    def __rmatmul__(self, other: 'Matrix'):
        return self.__matmul__(other)