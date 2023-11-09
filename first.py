import numpy as np
import matplotlib.pyplot as plt
import control as ct
import warnings
warnings.filterwarnings('ignore')

#plt.rcParams['figure.figsize']=[23, 10]
#plt.rcParams['font.size'] = 30

G1=ct.tf([2,5], [1,2,3])
G2=5*ct.tf(np.poly([-2,-5]),np.poly([-4,-5,-9]))
ct.minreal(G2)
ct.pzmap(G1)
#(A, B, C, D) = ct.ss(G1)
#print(G1,G2)
w = np.logspace(-1.5,1,200)
mag,phase,omega = ct.bode(G1,w,Hz=True,dB=True,deg=False)
#print(mag,phase,omega)
#ct.bode(G1)
(num,den) = ct.pade(0.25,3)
Gp = ct.tf(num,den)*G1
#print(Gp)
mag,phase,omega = ct.bode_plot(Gp)
out = ct.nyquist_plot(Gp)

H_simple = ct.tf([8], [1, 2, 2, 1])
F_saturation = ct.saturation_nonlinearity(1)
amp = np.linspace(1, 4, 10)
lines = ct.describing_function_plot(H_simple, F_saturation, amp)


t=np.linspace(0,10,100)

y=np.sin(t)
plt(t,y)