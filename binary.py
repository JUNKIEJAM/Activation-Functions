import numpy as np
import matplotlib.pyplot as plt

def binaryStep(x):
  x = np.linspace(-10, 10)
  plt.plot(x, binaryStep(x))
  plt.axis('tight')
  plt.title('Activation Function :binaryStep')
  plt.show()