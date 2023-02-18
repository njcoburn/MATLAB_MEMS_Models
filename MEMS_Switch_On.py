from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi, sqrt

e0=8.85418782e-12
V=42
go = 3e-6
E=78e9 #Au
I=(100e-6*(0.8e-6)**3)/12
l=300e-6
k2=3*E*I/(l**3)
l = 300e-6
t = 0.8e-6
w = 100e-6
k = 10 #k2 #10.0  # spring constant, N/m
m = 0.35*(w)*(l)*(t)*(19320) # mass, Kg
freq = 39.5e3
C1 = 1e-80
C2 = 1e-75
A = w**2 #w*l*0.75
td=150e-9
er=7.6
y = 0.06e-6  # lambda

    
def rlc(state,t,Q): 
    x, xd = state 
    g = x+go
    Fe = ((e0*A*(V**2))/((go+(td/er)+x)**2))*-0.5 #voltageSource
    Fc = ((C1*A)/(go+x)**3) - ((C2*A)/(go+x)**10)
    Qe = Q*((1.1-((x/go)**2))**(1.5))*(1+(9.638*((y/g)**1.159)))
    b = k/(2*pi*freq*Qe)   # damping coefficient, variable with Qe
    ks = (55e-6-k*go)/(go**3)
    #F = k*(go-x) + ks*(go-x)**3
    xdd = (Fe+Fc-(b*xd)-(k*x)-(ks*(x**3)))/m
    return [xd, xdd]

state0 = [0.0, 0.0]  #initial conditions [x0 , v0]  [m, m/sec] 

ti = 0.0  # initial time
tf = 25e-6  # final time
res = 10000 # steps
t = np.linspace(ti, tf, res)

Q=0.5


state = odeint(rlc, state0, t, args=(Q,))

x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

for i in range(len(x)):
    x[i] += go

index = np.argmin(abs(x))

#t_sort = np.array([])
#x_sort = np.array([])

#for i,j in enumerate(x):
#  if abs(x[i]) < 1000:
#    np.append(t_sort, t[i])
#    np.append(x_sort, x[i])

#print(len(t_sort))

###
###
###Plot###
###
###
###

fig ,ax1 = plt.subplots()

ax1.plot(t[0:(index+1)]*1e6,x[0:(index+1)]*1e6, 'b-',linewidth=3) #x and y plotted values multiplied by 1e6 to scale up for plotted units.

#plt.ylim(0,1.2)
#plt.xlim(0,3)


'''
Q=1.0
state = odeint(rlc, state0, t,args=(Q,))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])
for i in range(len(x)):
    x[i] += go
index = np.argmin(abs(x))
ax1.plot(t[0:(index+1)]*1e6,x[0:(index+1)]*1e6, 'b-',linewidth=3)
Q=2.0
state = odeint(rlc, state0, t,args=(Q,))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])
for i in range(len(x)):
    x[i] += go
index = np.argmin(abs(x))
ax1.plot(t[0:(index+1)]*1e6,x[0:(index+1)]*1e6, 'b-',linewidth=3)
'''
###plot parameters
plt.tick_params(direction='in',colors='k', axis='both', which='both',tick2On=True)
plt.minorticks_on()
ax1.set_xlabel('time ($\mu$s)')
ax1.set_ylabel('Gap Height ($\mu$m)', )#color='g')
#ax1.tick_params(axis='y', labelcolor='g')
'''
Q=2.0
state = odeint(rlc, state0, t,args=(Q,))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])
for i in range(len(x)):
    x[i] += go
ax1.plot(t*1e6,x*1e6, 'b:',linewidth=3)
###plot parameters
plt.tick_params(direction='in',colors='k', axis='both', which='both',tick2On=True)
plt.minorticks_on()
ax1.set_xlabel('time ($\mu$s)')
ax1.set_ylabel('Gap Height ($\mu$m)', )#color='g')
#ax1.tick_params(axis='y', labelcolor='g')
'''


#####ax2 for xd which is the velocity component

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.semilogy(t[0:index]*1e6,-xd[0:index], 'r-',linewidth=3)#t, xd)
plt.tick_params(direction='in',colors='k', axis='both', which='both',tick2On=True)
plt.minorticks_on()
ax2.set_ylabel('Velocity (m/s)', color='r')
ax2.tick_params(axis='y', labelcolor='r')
plt.ylim(0.01,10)


plt.savefig('ch3_working_pullin.pdf')