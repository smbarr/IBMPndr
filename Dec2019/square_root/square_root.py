#!/usr/bin/python

import os, sys
import numpy as np

x = np.linspace(-1,1,1000)
sr = np.full(1000,1000)

for n in range(1000):
  s = 10000.0*x[n]**2+1.0
  sr[n] = s/50.0
  for i in range(2):
    print(sr[n])
    sr[n] = (0.5*(sr[n]+s/sr[n]))

out = open("func.dat","w")
for n in range(1000):
  out.write("%e %e\n"%(x[n],sr[n]))
out.close()
