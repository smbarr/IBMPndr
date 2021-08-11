#!/usr/bin/env python3

import os, sys
import numpy as np
from scipy.optimize import fmin_slsqp
from scipy import optimize

def obj(x, *args):
  xa = np.linspace(-1,1,1000)
  f = 0.5+(x[0]*xa/(x[1]+(x[2]*xa**2/(x[3]+(x[4]*xa**2/(x[5]))))))
  l = (0.5*(xa-0.0526316)+0.0263158*np.sqrt(399.0*xa**2+1.0))/(xa)

  mse = np.square(np.subtract(f, l)).mean() 

  return mse

def print_fun(x, f, accepted):
  print("at minima %e accepted %d" % (f, int(accepted)))

x0 = [0.5, 3.0, 1.0, 5.0, 1.0, 7.0]
bounds = [(-1.0e10,1.0e10) for n in range(6)]

#out, fx, its, imode, smode = fmin_slsqp(obj, x0, bounds=bounds, full_output=2)
#
#print(out)
#print(fx)

minimizer_kwargs = {"method": "BFGS"}
#minimizer_kwargs = {"method": "Nelder-Mead"}
res = optimize.basinhopping(obj, x0, minimizer_kwargs=minimizer_kwargs, callback=print_fun)
print(res)
