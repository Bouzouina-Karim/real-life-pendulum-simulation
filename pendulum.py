import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.gridspec as gridspec

T=100
dt=0.01
N=int(T/dt)
t=np.linspace(0,T,N)
noise=0.5*np.random.randn(N)
print(noise.shape)
g=9.81
L=1
m=1.2
b=0.3
d=b/(m*(L**2))


s=np.zeros(N)
s[0]=0.3
s[1]=0.3

v_omega=np.zeros(N)
for i in range(1,N-1):
    omega = (s[i] - s[i-1]) / dt
    v_omega[i]=omega
    s[i+1]=((-(g/L)*np.sin(s[i])+noise[i])-d*omega)*dt**2+2*s[i]-s[i-1]
    

y=-L*np.cos(s)
x=L*np.sin(s)






fig=plt.figure(figsize=(12,6))
gs=gridspec.GridSpec(2,2,width_ratios=[1,1])

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[0, 1])
ax4 = fig.add_subplot(gs[1, 1])

ax1.plot(t,x,color='red',label='x(t)')
ax1.plot(t,y,color='green',label='y(t)')
ax1.set_title('Horizontal and Vertical Position vs Time')
ax1.legend()
ax1.grid(True)

ax2.plot(t,s,color='blue',label='θ(t)')
ax2.set_title('Angle vs Time')
ax2.legend()
ax2.grid(True)



ax3.set_xlim(-L-0.3,L+0.3)
ax3.set_ylim(-L-0.3,L+0.3)
ax3.set_title('Pendulum Animation')
ax3.set_aspect('equal')
ax3.grid()
line,=ax3.plot([],[],'o-',lw=3,label='pendulum')
ax3.legend()

ax4.plot(s,v_omega,label='f(θ(t))=w(t)')
ax4.set_title('Phase Space: θ vs ω')

ax4.legend()
ax4.grid(True)

def init():
    line.set_data([],[])
    return line,

def update(i):
    line.set_data([0,x[i]],[0,y[i]])
    return line,

ani=FuncAnimation(fig,update,frames=range(0, N, 5),init_func=init,blit=True,interval=33)
plt.show()
