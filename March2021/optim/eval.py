import random
import numpy as np

np.set_printoptions(linewidth=125)

grid = [[line.split()[j] for j in range(len(line.split()))] for line in open("grid")]

def calc_score(individual):
  hex_table = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
  }

  cost = 128
  imax = len(grid)
  jmax = len(grid[0])
  reward = [[0 for j in range(jmax)] for i in range(imax)]
  for i in range(imax):
    for j in range(jmax):
      reward[i][j] = 16*hex_table[grid[i][j][0]] + hex_table[grid[i][j][1]]
      reward[i][j] -= cost

  visited = [[True for j in range(jmax)] for i in range(imax)]
  positions = [int(n) for n in individual[:3]]
  heights = [int(n) for n in individual[3:]]
  for p, h in zip(positions, heights):
    w = h
    i = imax-1
    while w >= 1:
      if w > 1:
        for j in range(max(0,p-w), min(jmax,p+w)):
          visited[i][j] = False
      else:
        visited[i][p] = False
      w -= 1
      i -= 1

  print(np.array(visited))
  score = 0
  for i in range(imax):
    for j in range(jmax):
      if visited[i][j]:
        score += reward[i][j]
      
  print(score)
  return score,

individual = [11, 18, 8, 16, 15, 17, 0, 1, 10, 1, 0, 12, 0, 4, 16, 1, 0, 1, 0, 1]
print(calc_score(individual))
