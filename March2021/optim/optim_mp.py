import array
import multiprocessing
import sys
import random
import numpy as np
from deap import creator, base, tools, algorithms

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 19)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=20)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

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

  score = 0
  for i in range(imax):
    for j in range(jmax):
      if visited[i][j]:
        score += reward[i][j]
      
  #print(score)
  return score,

toolbox.register("evaluate", calc_score)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

if __name__ == "__main__":
    random.seed(42)
    
    # Process Pool of 4 workers
    pool = multiprocessing.Pool(processes=4)
    toolbox.register("map", pool.map)
    
    pop = toolbox.population(n=40000)
    hof = tools.HallOfFame(200)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=10, 
                        stats=stats, halloffame=hof)

    best_ind = tools.selBest(pop, 1)[0]
    print(best_ind)

    pool.close()
