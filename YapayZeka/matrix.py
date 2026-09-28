import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0.0 for _ in range(cols)] for _ in range(rows)]

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random.uniform(-1, 1)

    def display(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(round(self.data[i][j], 2), end=" ")
            print()

    @staticmethod
    def multiply(a, b):
        if a.cols != b.rows:
            print("ERROR: Matrix dimensions do not match!")
            return None

        result = Matrix(a.rows, b.cols)
        for i in range(a.rows):
            for j in range(b.cols):
                total = 0.0
                for k in range(a.cols):
                    total += a.data[i][k] * b.data[k][j]
                result.data[i][j] = total
        return result