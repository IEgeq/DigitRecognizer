import json
from matrix import Matrix


class ModelSaver:

  @staticmethod
  def save_model(network, filename='model.json'):
    data = {
        'layer1_weights': network.layer1.weights.data,
        'layer1_bias': network.layer1.bias.data,
        'layer2_weights': network.layer2.weights.data,
        'layer2_bias': network.layer2.bias.data,
    }

    with open(filename, 'w') as f:
      json.dump(data, f, indent=4)

    print(f"Model succesfully saved to '{filename}'")

  @staticmethod
  def load_model(network, filename='model.json'):
    with open(filename, 'r') as f:
      data = json.load(f)

    network.layer1.weights.data = data['layer1_weights']
    network.layer1.bias.data = data['layer1_bias']
    network.layer2.weights.data = data['layer2_weights']
    network.layer2.bias.data = data['layer2_bias']
