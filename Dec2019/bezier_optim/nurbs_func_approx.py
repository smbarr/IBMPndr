#!/usr/bin/env python3

import os, sys, math
import numpy as np

def u_x(x):
  u = ((0.5*(x-0.0526316))+(0.0263158*np.sqrt(399*x**2+1)))/x

  #u = (1.0/(20.0*x))+20.471
  #p = 0.699*x**6-1.364*x**4+1.156*x**2+0.05318
  #u = ((0.5*(x-0.0526316))+p)/x

  #u1 = (0.5*(x-0.0526316))
  #s = 399.0*x**2+1
  #u2 = 12*x**2+1.0
  #for i in range(5):
  #  u2 = 0.5*(u2+(s/u2))
  #  #u2 = (u2+(s/u2))
  #u = (u1 + 0.0263158*u2)/x

  #u = 0.5+(x/(1.0+x**2))
  #u = 0.5+2*x/(0.852294+((8.3416*x**2)/1.39703))
  #u = 0.5+300*x/(1.0+((100000*x**2)/1.39703))
  #u = 0.5+(3.32*x/(0.69855+(9.0*x**2/(0.48205+(15.457*x**2/10.218)))))-0.14*x**3
  return u

def x_u(u):
  #x = (2.0*u-1.0)/((1.0-u)**2+u**2+200.0*u*(1.0-u))
  x = (-0.1*(1.0-u)**2+0.1*u**2)/(0.1*(1.0-u)**2+4.0*u*(1.0-u)+0.1*u**2)
  #x = -0.010101*(x-0.5)/((x-1.00503)*(x+0.00502525))
  #x = -1.0/(300.0*u) - 1.0/(300.0*(u-1.0))
  #x = -1.0/(20.0*u) - 1.0/(20.0*(u-1.0))
  return x

def y_u(u):
  #y = ((1.0-u)**2+u**2)/((1.0-u)**2+100.0*(2.0*(1.0-u)*u)+u**2)
  y = (0.1*(1.0-u)**2+0.1*u**2)/(0.1*(1.0-u)**2+4.0*u*(1.0-u)+0.1*u**2)
  #y = (u*(0.010101-0.010101*u)-0.00505050505)/((u-1)*u-0.005050505)
  #y = 0.5/(5000.0*u**2) + 0.5/(5000.0*(u-1.0)**2)
  #y = 1.0/(230.0*u) - 1.0/(230.0*(u-1.0))
  #y = 1.0/(20.0*u) - 1.0/(20.0*(u-1.0))
  return y

x = np.linspace(-1,1,1000)
ab = np.abs(x)
y = np.zeros(1000)
#u = np.linspace(0.0,1.0,1000)
out = open("func.dat","w")
for n in range(len(x)):
  #x = x_u(u[n])
  #u = u_x(x[n])
  #y = y_u(u)
  u = u_x(x[n])
  y[n] = y_u(u)
  out.write("%e %e %e\n"%(x[n],y[n],ab[n]))
out.close()

mse = np.square(np.subtract(y,ab)).mean()
print(mse)
