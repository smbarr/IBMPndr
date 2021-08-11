#!/usr/bin/env python3

import os, sys
import numpy as np
from scipy.optimize import fmin_slsqp
from scipy import optimize

def obj(x, *args):
  all_pos = True
  for n in range(len(x)):
    if x[n] <= 0.0:
      all_pos = False
  mse = 10.0
  if all_pos:
    xa = np.linspace(-1,1,1000)
    f1 = np.log10(x[0]*xa**2+x[1])
    f2 = np.log10(x[2]*xa**2+x[3])
    f3 = np.log10(x[4]*xa**2+x[5])
    #f4 = np.log10(x[6]*xa**2+x[7])
    #x0 = x[5]*np.log10(x[1])+x[6]*np.log10(x[3])
    x0 = x[7]*np.log10(x[1])+x[8]*np.log10(x[3])+x[9]*np.log10(x[5])
    #x0 = x[9]*np.log10(x[1])+x[10]*np.log10(x[3])+x[11]*np.log10(x[5])+x[12]*np.log10(x[11])
    #f = x[8]*xa**2+x[9]*f1+x[10]*f2+x[11]*f3+x[12]*f4-x0
    f = x[6]*xa**2+x[7]*f1+x[8]*f2+x[9]*f3-x0
    #f = x[4]*xa**4+x[5]*f1+x[6]*f2-x0
    ab = np.abs(xa)

    mse = np.square(np.subtract(f, ab)).mean() 

  return mse

def print_fun(x, f, accepted):
  print("at minima %e accepted %d" % (f, int(accepted)))

x0 = [1.0 for n in range(10)]
#x0 = [1.12497144e+01, 2.83955036e-04, 9.06096029e+00, 1.11559160e-01,
#       8.53308814e-01, 6.87592361e-01, 1.25246186e-02, 1.62014524e-02,
#       1.83412236e-01, 1.59680853e+00]
#x0 = [3.15070384e+01, 4.50677261e-03, 1.94827390e+01, 3.25564706e-01,
#       1.28263979e+00, 6.27784847e-01, 1.53247749e-01, 2.95616173e-02,
#       1.73502913e-01, 8.74653133e-01]
#x0 = [5.11649541e+01, 7.38630737e-03, 1.71066528e+01, 3.06846358e-01,
#       1.48328873e+00, 6.27414116e-01, 1.85672906e-01, 3.06311077e-02,
#       1.74129543e-01, 7.42475452e-01]
#x0 = [1.15295487e+01, 1.41510437e-03, 1.61110367e+01, 2.56942708e-01,
#       1.47506489e+00, 6.09533745e-01, 1.82181301e-01, 2.83020892e-02,
#       1.67769123e-01, 7.56909788e-01]
#x0 = [4.87368891e+01, 5.86544076e-03, 2.28660770e+01, 3.47146122e-01,
#       1.66302644e+00, 5.79719843e-01, 2.08123633e-01, 2.79762458e-02,
#       1.60556173e-01, 6.62728372e-01]
#x0 = [4.29059237e+00, 4.81152619e-04, 3.53991516e+01, 4.95486287e-01,
#       1.70298105e+00, 5.80737790e-01, 2.05137773e-01, 2.69429102e-02,
#       1.54939965e-01, 6.73050068e-01]
#x0 = [5.76043530e+00, 5.88930258e-04, 5.52253684e+01, 7.15305886e-01,
#       1.92048946e+00, 6.03715456e-01, 2.13762610e-01, 2.58206434e-02,
#       1.49094397e-01, 6.45479588e-01]
#x0 = [7.64430460e+00, 5.95614888e-04, 5.69337734e+01, 5.37613114e-01,
#       2.19060384e+00, 5.26481604e-01, 2.38454266e-01, 2.23367431e-02,
#       1.27253349e-01, 5.78131533e-01]
#x0 = [7.93461508e+00, 5.44685283e-04, 5.91409692e+01, 5.32073741e-01,
#       2.25055451e+00, 5.38052665e-01, 2.38198985e-01, 2.11711160e-02,
#       1.26648160e-01, 5.80075107e-01]
#x0 = [1.31486278, 2.14677127, 5.42735959, 0.02280102, 0.10679375,
#       0.04171242, 0.94455642, 1.0140889 , 0.07224006, 0.20848166,
#       0.14040319, 0.86392181, 0.1994715 ]
#bounds = [(0.0,1.0e1) for n in range(13)]

#out, fx, its, imode, smode = fmin_slsqp(obj, x0, bounds=bounds, full_output=2)
#print(out)
#print(fx)

#minimizer_kwargs = {"method": "BFGS"}
minimizer_kwargs = {"method": "Nelder-Mead"}
res = 0.0
#res = optimize.basinhopping(obj, x0, minimizer_kwargs=minimizer_kwargs, callback=print_fun)
for n in range(20):
  res = optimize.basinhopping(obj, x0, minimizer_kwargs=minimizer_kwargs)
  x0 = res.x
  print(n,res.fun)
print(res.x)
