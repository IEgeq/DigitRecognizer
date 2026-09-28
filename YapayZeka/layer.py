from matrix import Matrix
from activation import Activation

class Layer:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size

        self.weights = Matrix(input_size, output_size)
        self.weights.randomize() 


        self.bias = Matrix(1, output_size)
        self.bias.randomize()

    def forward(self, input_data):
        self.input = input_data

        raw_output = Matrix.multiply(input_data, self.weights)

        for i in range(raw_output.rows):
            for j in range(raw_output.cols):
                raw_output.data[i][j] += self.bias.data[0][j]

        self.output = Activation.apply_sigmoid(raw_output)
        
        return self.output