import numpy as np
import matplotlib . pyplot as plt


a = np.zeros((40, 40))
b = np.ones((40, 40))

firstLine = np.hstack((a, b))
secondline = np.hstack((b, a))

ablje = np.vstack((firstLine, secondline))

print(ablje)
plt.imshow(ablje, cmap="gray")
plt.show()
