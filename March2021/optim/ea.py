#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# To assure reproductibility, the RNG seed is set prior to the items
# dict initialization. It is also seeded in main().
#random.seed(64)

# Create the item dictionary: item name is an integer, and value is 
# a (weight, value) 2-uple.
items = {}
# Create random items and store them in the items' dictionary.
for i in range(20):
    items[i] = random.randint(0, 19)

creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
creator.create("Individual", list, fitness=creator.Fitness)

toolbox = base.Toolbox()

# Attribute generator
toolbox.register("attr_item", random.randrange, 20)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, 
    toolbox.attr_item, 2000)
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
      
  return -1.0*score,

toolbox.register("evaluate", calc_score)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
toolbox.register("select", tools.selNSGA2)

def main():
    #random.seed(64)
    NGEN = 500
    MU = 2500
    LAMBDA = 100
    CXPB = 0.7
    MUTPB = 0.2
    
    pop = toolbox.population(n=MU)
    hof = tools.HallOfFame(10)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)
    
    algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats,
                              halloffame=hof)
    
    return pop, stats, hof
                 
if __name__ == "__main__":
    main()                 

