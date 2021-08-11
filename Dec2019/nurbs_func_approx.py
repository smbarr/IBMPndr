#!/usr/bin/env python3

import os, sys, math
import numpy as np

def x_u(u):
  x = (1.0-2.0*u)/(99998.0*(u-1.0)*u-1.0)
  return x

def y_u(u):
  y = -2.0000400008e-5*((u**2-u+0.5)/(u**2-u-1.0000200004e-5))
  return y

u = np.linspace(0.0,1.0,1000)
x = np.zeros(1000)
y = np.zeros(1000)
absolute_value = np.zeros(1000)
for n in range(len(u)):
  x[n] = x_u(u[n])
  y[n] = y_u(u[n])
  absolute_value[n] = np.abs(x[n])

mse = np.square(np.subtract(y,absolute_value)).mean()
print(mse)
