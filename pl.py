import matplotlib.pyplot as plt
import numpy as np

# Turn on interactive mode
plt.ion()

# Create some data
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Create a figure for each plot
fig1 = plt.figure()
plt.plot(x, y)
fig1.suptitle('Figure 1')
plt.show()

fig2 = plt.figure()
plt.plot(y, x)
fig2.suptitle('Figure 2')
plt.show()

fig3 = plt.figure()
plt.plot(x, y)
fig3.suptitle('Figure 3')
plt.show()

fig4 = plt.figure()
plt.plot(y, x)
fig4.suptitle('Figure 4')
plt.show()

# Keep all figures displayed
plt.show(block=True)
