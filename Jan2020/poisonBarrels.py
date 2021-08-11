#!/usr/bin/env python3

import os, sys
import numpy as np

seq = "B.DG;DF.AB;AH.CF;C.GH"

barrel_names = ["A", "B", "C", "D", "E", "F", "G", "H"]

nplants = 4
day1 = []
day2 = []
for n in range(len(seq.split(";"))):
  day1.append(seq.split(";")[n].split(".")[0])
  day2.append(seq.split(";")[n].split(".")[1])

#for b1 in barrel_names:
#  for b2 in barrel_names:
for bi1 in range(len(barrel_names)):
  for bi2 in range(bi1+1,len(barrel_names)):
    b1 = barrel_names[bi1]
    b2 = barrel_names[bi2]
    if not b1 == b2:
      plants = [[True for j in range(2)] for i in range(nplants)]
      for n in range(len(day1)):
        mixture = day1[n]
        if b1 in mixture or b2 in mixture:
          plants[n][0] = False
      for n in range(len(day2)):
        if plants[n][0]:
          mixture = day2[n]
          if b1 in mixture or b2 in mixture:
            plants[n][1] = False

      found_same = False

      for bti1 in range(len(barrel_names)):
        for bti2 in range(bti1+1,len(barrel_names)):
          bt1 = barrel_names[bti1]
          bt2 = barrel_names[bti2]
          #if not bt1 == b1 and not bt1 == b2 and not bt2 == b1 and not bt2 == b2 and not bt1 == bt2:
          if not bt1 == b1 and not bt2 == b2 and not bt1 == bt2:
            plants_test = [[True for j in range(2)] for i in range(nplants)]
            for n in range(len(day1)):
              mixture = day1[n]
              if bt1 in mixture or bt2 in mixture:
                plants_test[n][0] = False
            for n in range(len(day2)):
              if plants_test[n][0]:
                mixture = day2[n]
                if bt1 in mixture or bt2 in mixture:
                  plants_test[n][1] = False

            same = True
            for n in range(len(day1)):
              if not plants[n][0] == plants_test[n][0]:
                same = False
              if not plants[n][1] == plants_test[n][1]:
                same = False
            if same == True:
              found_same = True
        if found_same:
          print(b1,b2,found_same)
