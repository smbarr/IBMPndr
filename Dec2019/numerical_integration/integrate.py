#!/usr/bin/env python3

import os, sys
import numpy as np

def f(x):
  #f = 0.45*x**2+0.101038*np.log10(0.16*x**2+0.000247533)+0.220243*np.log10(0.6*x**2+0.0352894)-0.6843
  f = (0.9024*x**5+0.334436*x**3+0.00525218*x)/(x**4+0.0542033*x**2+0.000115652)

  return f

def integral(x):
  dx = 1.0e-3
  res = dx*(f(x)+f(x+dx))
  return res

x = np.linspace(-1,1,1000)
out = open("integral.dat","w")
f_int = 1.0
for n in range(1000):
  f_val = f(x[n])
  f_int += integral(x[n])
  out.write("%e %e %e\n"%(x[n],f_val,f_int))
out.close()
