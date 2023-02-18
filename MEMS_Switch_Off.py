#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 09:51:16 2020

@author: njcoburn
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi, sqrt

e0=8.85418782e-12
V=42*1.4
go = 3e-6
E=79e9
I=(100e-6*(0.8e-6)**3)/12
l=300e-6
k2=3*E*I/(l**3)
#print (k2)
F = 55e-6

l = 300e-6
t = 0.8e-6
w = 100e-6
k = 10#k2 #10.0  # spring constant, N/m
m = 0.35*(w)*(l)*(t)*(19320) # mass, Kg
freq = 39.5e3
C1 = 1e-80
C2 = 1e-75
A = w**2#w*l*0.75
y = 0.06e-6  # lambda

def rlc(state,t,Q): 
    x, xd = state 
    g =  go - x
    Qe = Q*((1.1-((x/go)**2))**(1.5))*(1+9.638*((y/g)**1.159))
    b = k/(2*pi*freq*Qe)   # damping coefficient
    #b = k/(2*pi*freq*Q)
    ks = (F-k*go)/(go**3)
    Fc = ((C1*A)/(go-x)**3) - ((C2*A)/(go-x)**10)
    #F = k*(go-x) + ks*(go-x)**3
    xdd = (Fc-(b*xd)-k*x-ks*(x**3))/m
    return [xd, xdd]

state0 = [-go, 0.0]  #initial conditions [x0 , v0]  [m, m/sec] 

ti = 0.0  # initial time
tf = 60e-6  # final time
res = 10000
t = np.linspace(ti, tf, res)

Q=0.5

state = odeint(rlc, state0, t, args=(Q,))

x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

###
###
###Plot###
###
###
###

fig ,ax1 = plt.subplots()

for i in range(len(x)):
    x[i] += go

ax1.plot(t*1e6,x*1e6, 'r-',linewidth=3, label='$Q = 0.5$') #x and y plotted values multiplied by 1e6 to scale up for plotted units.
#plt.ylim(0,1.2)


Q=1.0
state = odeint(rlc, state0, t,args=(Q,))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])
for i in range(len(x)):
    x[i] += go
ax1.plot(t*1e6,x*1e6, 'r--',linewidth=3, label='$Q = 1.0$')

Q=2.0
state = odeint(rlc, state0, t,args=(Q,))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])
for i in range(len(x)):
    x[i] += go
ax1.plot(t*1e6,x*1e6, 'r:',linewidth=3,label='$Q = 2.0$')



###plot parameters
plt.tick_params(direction='in',colors='k', axis='both', which='both',tick2On=True)
plt.minorticks_on()
ax1.set_xlabel('time ($\mu$s)')
ax1.set_ylabel('Gap Height ($\mu$m)', )#color='g')
#ax1.tick_params(axis='y', labelcolor='g')

# Now add the legend with some customizations.
legend = plt.legend(loc='lower right', shadow=False)
# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
#frame.set_facecolor('r')
frame.set_color('none')
frame.set_edgecolor('none')



'''
#####ax2 for xd which is the velocity component

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.plot(t*1e6,xd*1e6, 'b-',linewidth=3)#t, xd)
plt.tick_params(direction='in',colors='k', axis='both', which='both',tick2On=True)
plt.minorticks_on()
ax2.set_ylabel('Velocity (m/s)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

'''

