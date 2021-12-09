import numpy as np
import matplotlib.pyplot as plt

import cmath
def integration(x):
    a=np.exp(x)
    return sum(a)
    
def softmax(x):
    return np.exp(x)/integration(x)
    
x = np.linspace(-10, 10)
plt.plot(x, softmax(x))
plt.axis('tight')
plt.title('Activation Function :softmax')
plt.show()