from activation import Activation
from layer import Layer
from matrix import Matrix


class NeuralNetwork:

  def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate=0.1):
    self.layer1 = Layer(input_nodes, hidden_nodes)

    self.layer2 = Layer(hidden_nodes, output_nodes)

    self.learning_rate = learning_rate

  def predict(self, input_data):
    hidden_output = self.layer1.forward(input_data)
    final_output = self.layer2.forward(hidden_output)
    return final_output

  def train(self, input_data, target_data):
    hidden_output = self.layer1.forward(input_data)
    final_output = self.layer2.forward(hidden_output)

    output_errors = Matrix(1, target_data.cols)
    for i in range(target_data.cols):
      output_errors.data[0][i] = (
          target_data.data[0][i] - final_output.data[0][i]
      )

    for i in range(self.layer2.output_size):
      grad = Activation.sigmoid_derivative(final_output.data[0][i])
      grad *= output_errors.data[0][i] * self.learning_rate

      self.layer2.bias.data[0][i] += grad
      for j in range(self.layer2.input_size):
        self.layer2.weights.data[j][i] += grad * hidden_output.data[0][j]

    hidden_errors = Matrix(1, self.layer1.output_size)
    for i in range(self.layer1.output_size):
      error_sum = 0.0
      for j in range(self.layer2.output_size):
        error_sum += (
            output_errors.data[0][j] * self.layer2.weights.data[i][j]
        )
      hidden_errors.data[0][i] = error_sum

    for i in range(self.layer1.output_size):
      grad = Activation.sigmoid_derivative(hidden_output.data[0][i])
      grad *= hidden_errors.data[0][i] * self.learning_rate

      self.layer1.bias.data[0][i] += grad
      for j in range(self.layer1.input_size):
        self.layer1.weights.data[j][i] += grad * input_data.data[0][j]