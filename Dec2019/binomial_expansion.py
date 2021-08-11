#!/usr/bin/env python3

import os, sys, math
import numpy as np

def factorial(x):
  res = 1.0
  for n in range(x,0,-1):
    res *= float(n)
  return res

x = np.linspace(-1,1,1000)
ab = np.zeros(1000)
for n in range(1000):
  ab = 1.0
  ab += ((x**2-1.0)/2.0)
  for i in range(2,30):
    ab -= (factorial(2*i-3)*(1.0-x**2)**i)/(2**(2*i-2)*factorial(i-2)*factorial(i))

out = open("func.dat","w")
for n in range(1000):
  out.write("%e %e\n"%(x[n],ab[n]))
out.close()
  
