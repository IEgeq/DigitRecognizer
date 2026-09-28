import os
import sys
import warnings

warnings.filterwarnings('ignore')

from activation import Activation
from matrix import Matrix
from model_saver import ModelSaver
from network import NeuralNetwork
from PIL import Image


def predict_image(image_path):
  script_dir = os.path.dirname(os.path.abspath(__file__))
  model_path = os.path.join(script_dir, 'model.json')

  nn = NeuralNetwork(input_nodes=784, hidden_nodes=64, output_nodes=10)
  ModelSaver.load_model(nn, model_path)

  img = Image.open(image_path).convert('L')
  img = img.resize((28, 28))


  if hasattr(img, 'get_flattened_data'):
    pixels = list(img.get_flattened_data())
  else:
    pixels = list(img.getdata())

  img_matrix = Matrix(1, 784)
  img_matrix.data = [[p / 255.0 for p in pixels]]

  outputs = nn.predict(img_matrix)

  max_val = -1.0
  predicted_digit = -1

  for i in range(10):
    val = outputs.data[0][i]
    if val > max_val:
      max_val = val
      predicted_digit = i

  sys.stdout.write(f'{predicted_digit}')


if __name__ == '__main__':
  if len(sys.argv) > 1:
    img_path = sys.argv[1]
    predict_image(img_path)