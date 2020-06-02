# from population import *
import random

from DNA import DNA


class Main(DNA):
    def __init__(self):
        DNA.__init__(self)
        self.matingPool = []
        for i in range(len(self.population)):
            self.population[i].fitness()

        for i in range(len(self.population)):
            n = self.population[i].fitness * 100

            for j in range(n):
                self.matingPool.append(self.population[i])

    def reproduction(self):
        a = random.randrange(0, len(self.matingPool) + 1)
        b = random.randrange(0, len(self.matingPool) + 1)

        while True:
            parentA = self.matingPool[a]
            parentB = self.matingPool[b]

            if not parentA == parentB:
                break

        child = parentA.crossover(parentB)
        child.mutate()
        return child


while True:
    ob = Main()
    gene = ob.reproduction()
    print(gene.genes)



