import numpy as np
import matplotlib.pyplot as plt

def signum(x):
    
    return 2*np.heaviside(x,1)-1
    
x = np.linspace(-10, 10)
plt.plot(x, signum(x))
plt.axis('tight')
plt.title('Activation Function :signum')
plt.show()