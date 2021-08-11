#!/usr/bin/env python3

import os, sys, math
import numpy as np

x = np.linspace(-1,1,11)
ab = np.abs(x)

out = open("pnts.txt","w")
for n in range(11):
  out.write("%e,%e,0.0\n"%(x[n],ab[n]))
out.close()
