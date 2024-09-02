import numpy as np
import matplotlib.pyplot as plt

#Physics
Lx = 10 # length of domain in x direction, m
D = 1 #% Diffusion coefficient
tt = 1 #% total time of simulation in s

#% Preprocessing
nx = 200 #% number of grid points
dx = Lx/(nx-1) #% spacing between points, m
X = np.arange(-Lx/2,Lx/2,dx) #% vectorized positions of gridpoints
dt = 1e-3 #% time interval 
nt = round(tt/dt) #% number of time intervals

#% Initial conditions
C0 = 1 #% Concentration amplitude
w = 1 #% Concentration width
cx = 0; #% Location of amplitude center in x direction
C = C0 * np.exp(-(X-cx)**2/w)
time = 0; #% initial time, s

#% Action
fig, ax = plt.subplots()
plt.ylim(0, 1)
for it in range(nt):
    dCdt = D * np.diff(np.diff(C)/dx)/dx
    C[1:-1] = C[1:-1] + dCdt * dt
    time = time + dt
    #%postprocessing
    if it%10 == 1:       
        plt.cla()
        plt.ylim(0, 1)           
        ax.scatter(X,C,c=C,vmin=0, vmax=1)
        plt.pause(0.01)
       

plt.show()