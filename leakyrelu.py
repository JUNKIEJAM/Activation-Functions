from matplotlib import pyplot as plt
import numpy as np

def lrelu_forward(x):
    return np.where(x > 0, x, x * 0.1)


x = np.random.rand(10) - 0.5
x = np.append(x, 0.0)
x = np.sort(x)
y = lrelu_forward(x)

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Plot of the Leaky RELU")
plt.show()   