from sklearn.datasets import fetch_openml
from matrix import Matrix
from model_saver import ModelSaver
from network import NeuralNetwork


def train_on_mnist():
  print("Downloading MNIST dataset (this may take a couple of seconds)...")

  mnist = fetch_openml(
      "mnist_784", version=1, as_frame=False, parser="liac-arff"
  )
  X, y = mnist.data, mnist.target.astype(int)

  X = X / 255.0

  nn = NeuralNetwork(
      input_nodes=784, hidden_nodes=64, output_nodes=10, learning_rate=0.2
  )

  print("Training is starting...")
  sample_count = 1000  

  for i in range(sample_count):
    img_matrix = Matrix(1, 784)
    img_matrix.data = [X[i].tolist()]

    target_matrix = Matrix(1, 10)
    target_matrix.data = [[0.0] * 10]
    label = y[i]
    target_matrix.data[0][label] = 1.0

    nn.train(img_matrix, target_matrix)

    if (i + 1) % 200 == 0:
      print(f"{i + 1}/{sample_count} pictures done...")

  print("Training succesfully done!")

  ModelSaver.save_model(nn, "model.json")


if __name__ == "__main__":
  train_on_mnist()