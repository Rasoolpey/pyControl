import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(1, figsize=(5,5))

delta = 0.025
x,y = np.meshgrid(np.arange(-4,4.1,delta),np.arange(-4,4.1,delta))
print(x,y)

f1 = x**2 + y-5
f2 = x**2 + y**2 - 7

plt.contour(x,y,f1,[0])
plt.contour(x,y,f2,[0])
plt.show()