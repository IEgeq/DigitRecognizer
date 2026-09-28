import math
from matrix import Matrix


class Activation:

  @staticmethod
  def sigmoid(x):
    x = max(-500, min(500, x))
    return 1.0 / (1.0 + math.exp(-x))

  @staticmethod
  def sigmoid_derivative(x):
    return x * (1.0 - x)

  @staticmethod
  def apply_sigmoid(matrix):
    result = Matrix(matrix.rows, matrix.cols)
    for i in range(matrix.rows):
      for j in range(matrix.cols):
        result.data[i][j] = Activation.sigmoid(matrix.data[i][j])
    return result