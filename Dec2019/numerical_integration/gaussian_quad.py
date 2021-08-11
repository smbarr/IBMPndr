#!/usr/bin/python

import os, sys
import numpy as np


def f(x):
  f = (0.9024*x**5+0.334436*x**3+0.00525218*x)/(x**4+0.0542033*x**2+0.000115652)
  return f

def integral(x):
  dx = 1.0e-3
  res = dx*(f(x)+f(x+dx))
  return res

