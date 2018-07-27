# Try out MatPlotLib in VS Code 

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

try:
    min=int(input("Min Limit:"))
    max=int(input("Max Limit:"))
except ValueError:
    print("Please enter a valid number")

x = np.linspace(min,min+20, max)
plt.plot(x, np.sin(x))
plt.show()
