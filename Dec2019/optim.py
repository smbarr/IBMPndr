#!/usr/bin/env python3

import os, sys
import numpy as np
from scipy.optimize import fmin_slsqp
from scipy import optimize

#a0/(x*x*x*x)+a1/(x*x)+a2*(x*x)+a3*(x*x*x*x)
#a0/(x*x*x)+a1/(x*x)+a2/x+a3+a4*x+a5*(x*x)+a6(x*x*x)
#a0*(x*x)+a1*(x*x*x*x)+a2*(x*x*x*x*x*x)

def func(x, coeffs):
  #res = coeffs[0]/(x**4)+coeffs[1]/(x**2)+coeffs[2]*(x**2)+coeffs[3]*(x**4)
  #res = coeffs[0]/(x**3)+coeffs[1]/(x**2)+coeffs[2]/(x**1)+coeffs[3]*x+coeffs[4]*x**2+coeffs[5]*x**3
  res = coeffs[0]/(x**2)+coeffs[1]/(x**1)+coeffs[2]*x+coeffs[3]*x**2+coeffs[4]*x**3
  #res = coeffs[0]/(x**3)+coeffs[1]/(x**2)+coeffs[2]/(x**1)+coeffs[3]*x+coeffs[4]*x**2
  return res

def func_p(x, coeffs):
  #res = -4.0*coeffs[0]/(x**5)-2.0*coeffs[1]/(x**3)+2.0*coeffs[2]*x+4.0*coeffs[3]*(x**3)
  #res = -3.0*coeffs[0]/(x**4)-2.0*coeffs[1]/(x**3)-1.0*coeffs[2]/(x**2)+coeffs[3]+2.0*coeffs[4]*x+3.0*coeffs[5]*x**2
  res = -2.0*coeffs[0]/(x**3)-1.0*coeffs[1]/(x**2)+coeffs[2]+2.0*coeffs[3]*x+3.0*coeffs[4]*x**2
  #res = -3.0*coeffs[0]/(x**4)-2.0*coeffs[1]/(x**3)-1.0*coeffs[2]/(x**2)+coeffs[3]+2.0*coeffs[4]*x
  return res

def func_2p(x, coeffs):
  #res = 20.0*coeffs[0]/(x**6)+6.0*coeffs[1]/(x**4)+2.0*coeffs[2]+12.0*coeffs[3]*(x**2)
  #res = 12.0*coeffs[0]/(x**5)+6.0*coeffs[1]/(x**4)-2.0*coeffs[2]/(x**3)+2.0*coeffs[4]+6.0*coeffs[5]*x
  res = 6.0*coeffs[0]/(x**4)-2.0*coeffs[1]/(x**3)+2.0*coeffs[2]+6.0*coeffs[3]*x
  #res = 12.0*coeffs[0]/(x**5)+6.0*coeffs[1]/(x**4)-2.0*coeffs[2]/(x**3)+2.0*coeffs[4]
  return res

def obj(x, *args):
  xa = np.linspace(-1,1,1000)
  #xa[999] += 1.0e-4
  #root = get_root(x)
  #root_val = func(root, x)
  #f = x[0]/((xa)**4)+x[1]/((xa)**2)+x[2]*((xa)**2)+x[3]*((xa)**4)
  #f = x[0]/((xa+root)**4)+x[1]/((xa+root)**2)+x[2]*((xa+root)**2)+x[3]*((xa+root)**4)-root_val
  #f = x[0]/((xa+root)**3)+x[1]/((xa+root)**2)+x[2]/((xa+root))+x[3]*(xa+root)+x[4]*(xa+root)**2+x[5]*(xa+root)**3-root_val
  f = x[0]/((xa+x[5])**4)+x[1]/((xa+x[6])**2)+x[2]*((xa+x[7])**4)+x[3]*(xa+x[8])**2+x[4]*(xa+x[9])**3-x[10]
  #f = x[0]/((xa+root)**3)+x[1]/((xa+root)**2)+x[2]/((xa+root))+x[3]*(xa+root)+x[4]*(xa+root)**2-root_val
  #f = x[0]*(xa**2)+x[1]*(xa**4)+x[2]*(xa**6)
  ab = np.abs(xa)

  mse = np.square(np.subtract(f, ab)).mean() 

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

x0 = [1.0 for n in range(11)]
#x0 =[ 79.41705176, 260.26770716, 201.00189787,  57.81367526, 6.29242123]
#x0 = [ 2.94710648e+00, -1.62312550e+04,  1.78064871e+04,  2.78870873e+03, 2.59707004e+02,  8.88940433e+00]
#x0 = [-6.39584813e+01,  5.45089466e+01,  1.19510631e+00, -2.72151244e-02]
#x0 = [-2.10285628e-07,  5.12719405e-04,  2.13223022e+00, -1.22377051e+00]
bounds = [(-1.0e10,1.0e10) for n in range(5)]

#print(func(0.0, [1.0, 2.0, 1.0, 1.0], [-1.0, -1.0, -1.0, -1.0, -4.0]))
#print(func(-1.0, [1.0, 2.0, 1.0, 1.0], [0.0, 0.0, 0.0, 0.0, -4.0]))
#print(func(-1.0, [1.0, 2.0, 1.0, 1.0]))
#root = get_root(x0)
#print(root)
#print(func(root, x0))

#out, fx, its, imode, smode = fmin_slsqp(obj, x0, bounds=bounds, full_output=2)
#
#print(out)
#print(fx)

minimizer_kwargs = {"method": "BFGS"}
#minimizer_kwargs = {"method": "Nelder-Mead"}
res = optimize.basinhopping(obj, x0, minimizer_kwargs=minimizer_kwargs, callback=print_fun)
print(res)
