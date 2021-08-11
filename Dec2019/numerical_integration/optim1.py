#!/usr/bin/env python3

import os, sys
import numpy as np
from scipy.optimize import fmin_slsqp
from scipy import optimize

def obj(x, *args):
  xa = np.linspace(-1,1,1000)
  #f = x[0]*xa**2/(x[1]+(x[2]*xa**2/(x[3]+x[4]**2)))+x[5]*xa**2-3.606
  f = x[0]*xa**2/(x[1]+(x[2]*xa**2))+x[3]*xa**2-3.225
  f2 = np.log10(7.644*xa**2+0.0005956)

  mse = np.square(np.subtract(f,f2)).mean() 

  #print(mse)
  return mse

def get_root(coeffs):
  x = -1.0e2
  dx = 1.0e-4
  resid = 1.0e10
  itr = 1
  while resid > 1.0e-10:
    f = func_p(x, coeffs)
    fp = func_2p(x, coeffs)
    old_x = x
    x = x - f/fp
    resid = abs(x-old_x)
    itr += 1
    if itr > 20:
      x = -20
      break

  return x

def print_fun(x, f, accepted):
  print("at minima %e accepted %d" % (f, int(accepted)))

#x0 = [0.45, 0.101038, 0.16, 0.000247533,
#      0.220243, 0.6, 0.0352894, 0.6843]
x0 = [5.0, 0.01, 1.0, 1.0]
bounds = [(0.0,1.0e10) for n in range(4)]

#out, fx, its, imode, smode = fmin_slsqp(obj, x0, bounds=bounds, full_output=2)
#print(out)
#print(fx)
#
for n in range(10):
  minimizer_kwargs = {"method": "BFGS"}
  #minimizer_kwargs = {"method": "Nelder-Mead"}
  #res = optimize.basinhopping(obj, x0, minimizer_kwargs=minimizer_kwargs, callback=print_fun)
  res = optimize.basinhopping(obj, x0, minimizer_kwargs=minimizer_kwargs)
  x0 = res.x
  print(n,res.fun)
