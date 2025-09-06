import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0, 15, 100)
print(x)

fig, axes = plt.subplots()
axes.hist(x, bins=15)
plt.show()