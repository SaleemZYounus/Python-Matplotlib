import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2, 3, 4, 5, 6, 7, 8, 9])
ypoints = np.array([3, 3, 3, 5, 1, 3, 3, 3])

plt.title("Heart Beat Plot")
plt.plot(xpoints, ypoints)
plt.show()

