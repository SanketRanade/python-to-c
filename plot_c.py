import numpy as np
import matplotlib.pyplot as plt

elips = np.loadtxt('ellipse.dat',dtype='double')
P = np.loadtxt('x_P.dat',dtype='double')
Q = np.loadtxt('x_Q.dat',dtype='double')

plt.plot(elips[0,:],elips[1,:],label='ELLIPSE')
plt.plot(P[0,:],P[1,:],label='$N_1$')
plt.plot(Q[0,:],Q[1,:],label='$N_2$')


plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()
plt.legend(loc='best')
plt.axis('equal')
plt.show()
