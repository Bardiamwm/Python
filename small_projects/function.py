import numpy as np
import matplotlib.pyplot as mt

x = np.linspace(-10, 10, num=133)
y = abs(x)

mt.plot(x, y)
mt.show()