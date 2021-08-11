#!/usr/bin/python

import os, sys
import numpy as np

def integral(x):
  #res = x*(0.9+(0.191301/(x**2+0.0588156))+(0.0877605/(x**2+0.00154708)))
  res = 0.1*np.sin(-2.0*x)
  return res

out = open("derivative.dat","w")
dx = 1.0e-3
x = np.linspace(-1,1,1000)
for n in range(1000):
  f1 = integral(x[n])
  f2 = integral(x[n]+dx)
  f = (f2-f1)/dx
  out.write("%e %e %e\n"%(x[n],f,f1))
out.close()
