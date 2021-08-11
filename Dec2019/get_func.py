#!/usr/bin/env python

import os, sys, math
import numpy as np

x = np.linspace(-1,1,1000)
f1 = 0.0263158*np.sqrt(399.0*x**2+1.0)-5.0*x**2
#f1 = 0.0263158*np.sqrt(399.0*x**2+1.0)
#f2 = 99.0*x**2+1.0
#f = f1 - f2
f = f1

z = np.polyfit(x,f1,6)
p = np.poly1d(z)
print(p)
py = p(x)
mse = np.square(np.subtract(f, py)).mean() 
print(mse)
