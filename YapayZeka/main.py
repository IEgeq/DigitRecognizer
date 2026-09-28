from matrix import Matrix
from network import NeuralNetwork

if __name__ == "__main__":
  # Neural Network architecture: 784 Input -> 64 Hidden -> 10 Output Neurons
  nn = NeuralNetwork(784, 64, 10, learning_rate=0.5)

  # Generate random test input vector (1x784)
  inputs = Matrix(1, 784)
  inputs.randomize()

  # Target output vector (One-Hot Encoding for digit '3')
  targets = Matrix(1, 10)
  targets.data = [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

  print("--- PRE-TRAINING PREDICTION ---")
  prediction_before = nn.predict(inputs)
  print(f"Probability of Neuron #3: {prediction_before.data[0][3]:.4f}")

  print("\nTraining (1000 Iterations)...")
  for _ in range(1000):
    nn.train(inputs, targets)

  print("\n--- POST-TRAINING PREDICTION ---")
  prediction_after = nn.predict(inputs)
  print(f"Probability of Neuron #3: {prediction_after.data[0][3]:.4f}")