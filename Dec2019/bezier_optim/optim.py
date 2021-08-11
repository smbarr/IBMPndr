#!/usr/bin/env python3

import os, sys
import numpy as np
from scipy.optimize import fmin_slsqp
from scipy import optimize

def obj(x, *args):
  degree = 5
  nmax = 1000
  y = np.zeros(1000)
  du = 1.0/(float(nmax)-1.0)
  
  w = [1.0 for n in range(degree)]
  p_x = [-1.0, x[0], x[2], -1.0*x[0], 1.0]
  p_y = [ 1.0, -1.0*x[1], x[3], -1.0*x[1], 1.0]
  curve = [[0.0 for j in range(2)] for n in range(nmax)]
  ab = np.zeros(nmax)
  for n in range(nmax):
    u = du*float(n)
    B = [0.0 for n in range(degree)]
  
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
    y[n] = numer_y/denom_y
    ab[n] = np.abs(curve[n][0])
  mse = np.square(np.subtract(y, ab)).mean() 

  print(mse)
  return mse

def print_fun(x, f, accepted):
  print("at minima %e accepted %d" % (f, int(accepted)))

x0 = [1.0, 0.0, 1.0, 0.0, 0.0]
bounds = [(-2.0, 2.0) for n in range(5)]

#print(func(0.0, [1.0, 2.0, 1.0, 1.0], [-1.0, -1.0, -1.0, -1.0, -4.0]))
#print(func(-1.0, [1.0, 2.0, 1.0, 1.0], [0.0, 0.0, 0.0, 0.0, -4.0]))
#print(func(-1.0, [1.0, 2.0, 1.0, 1.0]))
#root = get_root(x0)
#print(root)
#print(func(root, x0))

out, fx, its, imode, smode = fmin_slsqp(obj, x0, bounds=bounds, full_output=2)

print(out)
print(fx)

#minimizer_kwargs = {"method": "BFGS"}
##minimizer_kwargs = {"method": "Nelder-Mead"}
#res = optimize.basinhopping(obj, x0, minimizer_kwargs=minimizer_kwargs, callback=print_fun)
#print(res)
