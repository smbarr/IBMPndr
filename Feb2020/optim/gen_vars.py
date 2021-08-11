#!/usr/bin/env python

import os, sys

s = "  initial_point ="
for n in range(20):
  s += " 1"

print(s)

s = "  lower_bounds ="
for n in range(20):
  s += " 1"

print(s)

s = "  upper_bounds ="
for n in range(20):
  s += " 100"

print(s)

s = "  descriptors ="
for n in range(20):
  s += " 'cl_%d'"%(n+1)

print(s)
