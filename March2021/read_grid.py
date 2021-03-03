import os, sys
import numpy as np

def calc_reward(grid):
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
  return reward

def sum_visited(row):
  unique, counts = np.unique(np.array(row), return_counts=True)
  try:
    n_visited = dict(zip(unique, counts))[True]
  except:
    n_visited = 0
  return n_visited

def eval_path(reward, path):
  imax = len(reward)
  jmax = len(reward[0])
  visited = [[False for j in range(jmax)] for i in range(imax)]

  valid = True

  init = path[0]
  if not init[0] == 0:
    valid = False

  score = reward[init[0]][init[1]]
  visited[init[0]][init[1]] = True
  reward[init[0]][init[1]] = 0
  cnt = 1
  while cnt < len(path):
    if not path[cnt][0] == path[cnt-1][0]:
      n_visited = sum_visited(visited[path[cnt-1][0]])
      if not n_visited == jmax:
        valid = False
        break
      else:
        score += reward[path[cnt][0]][path[cnt][1]]
        visited[path[cnt][0]][path[cnt][1]] = True
        reward[path[cnt][0]][path[cnt][1]] = 0
    else:
      score += reward[path[cnt][0]][path[cnt][1]]
      visited[path[cnt][0]][path[cnt][1]] = True
      reward[path[cnt][0]][path[cnt][1]] = 0
    cnt += 1

  if not valid:
    score = 0

  return score
      
grid = [[line.split()[j] for j in range(len(line.split()))] for line in open("grid")]
reward = calc_reward(grid)

path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
score = eval_path(reward, path)
print(score)
