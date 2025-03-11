import numpy as np

from matplotlib import pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)


y = np.sin(x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine Curve")
plt.show()


plt.plot(np.random.randn(1000).cumsum())
plt.show()
