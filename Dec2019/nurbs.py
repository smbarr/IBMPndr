#!/usr/bin/env python3

import os, sys
import math
import numpy as np

degree = 5
nmax = 1000
y = np.zeros(1000)
du = 1.0/(float(nmax)-1.0)

w = [1.0 for n in range(degree)]
#w[2] = 100.0

#p_x = [-1.0, 1.0, -1.0, 1.0]
#p_y = [1.0, -1.0, -1.0, 1.0]
p_x = [-1.0, 0.30470625, 0.0, -0.30470625, 1.0]
p_y = [1.0, -0.31286666, 0.18312048, -0.31286666, 1.0]

#[ 0.41818574 -0.4081582  -0.28770735 -0.26259639]

out = open("curve.dat","w")
B_str = ["" for n in range(degree)]
curve = [[0.0 for j in range(2)] for n in range(nmax)]

#B_str[0] = "((1.0-x)**8)"
#B_str[1] = "(8.0*x**1*(1.0-x)**7)"
#B_str[2] = "(8.0*x**2*(1.0-x)**6)"
#B_str[3] = "(8.0*x**3*(1.0-x)**5)"
#B_str[4] = "(8.0*x**4*(1.0-x)**4)"
#B_str[5] = "(8.0*x**5*(1.0-x)**3)"
#B_str[6] = "(8.0*x**6*(1.0-x)**2)"
#B_str[7] = "(8.0*x**7*(1.0-x))"
#B_str[8] = "(x**8)"

B_str[0] = "((1.0-x)^4)"
B_str[1] = "(4.0*x*(1.0-x)^3)"
B_str[2] = "(4.0*x^2*(1.0-x)^2)"
B_str[3] = "(4.0*x^3*(1.0-x))"
B_str[4] = "(x^4)"

numer_str = "("+B_str[0]+"*("+str(p_y[0])+")"
denom_str = "("+B_str[0]
for i in range(1,degree):
  numer_str += "+"+B_str[i]+"*("+str(p_y[i])+")"
  denom_str += "+"+B_str[i]

print(numer_str+")/"+denom_str+")")

ab = np.zeros(nmax)
x = np.linspace(-1,1,nmax)
for n in range(nmax):
  u = du*float(n)
  B = [0.0 for n in range(degree)]
  #B[0] = (1.0-u)**8
  #B[1] = 8.0*u**1*(1.0-u)**7
  #B[2] = 8.0*u**2*(1.0-u)**6
  #B[3] = 8.0*u**3*(1.0-u)**5
  #B[4] = 8.0*u**4*(1.0-u)**4
  #B[5] = 8.0*u**5*(1.0-u)**3
  #B[6] = 8.0*u**6*(1.0-u)**2
  #B[7] = 8.0*u**7*(1.0-u)
  #B[8] = u**8

  B[0] = (1.0-u)**4
  B[1] = 4.0*u**1*(1.0-u)**3
  B[2] = 4.0*u**2*(1.0-u)**2
  B[3] = 4.0*u**3*(1.0-u)
  B[4] = u**4
  numer_x = 0.0
  denom_x = 0.0
  numer_y = 0.0
  denom_y = 0.0
  for i in range(degree):
    numer_x += B[i]*w[i]*p_x[i]
    denom_x += B[i]*w[i]
    numer_y += B[i]*w[i]*p_y[i]
    denom_y += B[i]*w[i]
  curve[n][0] = numer_x/denom_x
  #curve[n][1] = numer_y/denom_y
  y[n] = numer_y/denom_y
  ab[n] = np.abs(curve[n][0])
  #out.write("%e %e\n"%(curve[n][0],y[n]))
  out.write("%e %e %e\n"%(x[n],curve[n][0],y[n]))
out.close()

mse = np.square(np.subtract(y,ab)).mean()
print(mse)
