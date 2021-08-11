#!/usr/bin/env python3

import os, sys, math
import numpy as np

def cheb_2(x):
  T_0 = 1.0
  T_1 = x
  T_2 = 2.0*x*T_1-T_0

  return T_2

x = np.linspace(-1,1,1000)
ab = np.zeros(1000)

for n in range(1000):
  ab[n] = 0.5
  for i in range(1,50):
    ab[n] += (((-1.0)**(i+1)/(4.0*i**2-1.0))*cheb_2(x[n]))
  ab[n] *= (4.0/np.pi)

out = open("func.dat","w")
for n in range(1000):
  out.write("%e %e\n"%(x[n],ab[n]))
out.close()
