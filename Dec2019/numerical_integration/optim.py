#!/usr/bin/env python3

import os, sys
import numpy as np
from scipy.optimize import fmin_slsqp
from scipy import optimize

def obj(x, *args):
  xa = np.linspace(-1,1,1000)
  f1 = (xa**2/(x[0]+x[1]*xa**2))+x[2]*xa**2
  f2 = (xa**2/(x[3]+x[4]*xa**2))+x[5]*xa**2
  f3 = (xa**2/(x[6]+x[7]*xa**2))+x[8]*xa**2
  #f4 = (xa**2/(x[9]+x[10]*xa**2))+x[11]*xa**2
  f = x[9]*xa**2+x[10]*f1+x[11]*f2+x[12]*f3
  ab = np.abs(xa)

  mse = np.square(np.subtract(f, ab)).mean() 

  #print(mse)
  return mse

def print_fun(x, f, accepted):
  print("at minima %e accepted %d" % (f, int(accepted)))

x0 = [1.0 for n in range(13)]

#out, fx, its, imode, smode = fmin_slsqp(obj, x0, bounds=bounds, full_output=2)
#print(out)
#print(fx)

minimizer_kwargs = {"method": "BFGS"}
#minimizer_kwargs = {"method": "Nelder-Mead"}
res = optimize.basinhopping(obj, x0, minimizer_kwargs=minimizer_kwargs, callback=print_fun)
print(res)
