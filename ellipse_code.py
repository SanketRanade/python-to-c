import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Plotting ellipse
len=100
theta=np.linspace(0,2*np.pi,len)
#Given ellipse parameters
#Eqn : x.T@V@x + 2u.T@x+F=0
V=np.array(([1,0],[0,3]))
u=np.array([0,0])
F=-9
O=np.array([0,0])
l,m=LA.eig(V/-F)
y = np.zeros((2,len))
a=1/l[0]**0.5
b=1/l[1]**0.5
print(a)
print(b)

y[0,:] = a*np.cos(theta)
y[1,:] = b*np.sin(theta)

#Define function for line
def line_dir_pt(m,A,k1,k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#Generating lines
n1 = np.array([(3/(2**0.5)),(3*(1.5**0.5))])
n2 = np.array([3/(2**0.5),(1.5**0.5)])
x_N1 = line_dir_pt(n1,n2,-1.4,0.6)

n3 = np.array([(-3/(2**0.5)),(3*(1.5**0.5))])
n4 = np.array([-3/(2**0.5),(1.5**0.5)])
x_N2 = line_dir_pt(n3,n4,-1.4,0.6)

#Plotting all lines and ellipse
plt.plot(x_N1[0,:],x_N1[1,:],label='$N_1$')
plt.plot(x_N2[0,:],x_N2[1,:],label='$N_2$')
plt.plot(y[0,:],y[1,:],label='ELLIPSE')

plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 - 0.1), O[1] * (1 + 0.1) , 'O')
plt.plot(n2[0], n2[1], 'o')
plt.text(n2[0] * (1 + 0.1), n2[1] * (1 - 0.1) , 'P')
plt.plot(n4[0], n4[1], 'o')
plt.text(n4[0] * (1 - 0.1), n4[1] * (1-0.2) , 'Q')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()
plt.legend(loc='best')
plt.axis('equal')
plt.show()
