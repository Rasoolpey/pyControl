import matplotlib as plt
import numpy as np


fig = plt.figure(1, figsize=(5,5))

delta = 0.025
x,y = np.meshgrid(np.arange(-4,4.1,delta),np.arange(-4,4.1,delta))