#!/usr/bin/env python3

import os, sys
import numpy as np

x = np.linspace(-1,1,1000)
a = np.abs(x)
f = (x+1.0)/2.0
#f = np.sin(3.07*np.cos(x))

mse = np.square(np.subtract(a, f)).mean()
print(mse)
