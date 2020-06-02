import random
import sys

state = True
target = list("to be or not to be")
# target = list("aaaaaaaaaaaaaa")
generation = 0
# sys.setrecursionlimit(10 ** 6)
population = []
matingPool = []
totalPopulation = 200


class DNA:
    def __init__(self):
        self.genes = []
        self.target = target
        self.fitness = None
        self.mutationRate = 1

        for i in range(len(self.target)):
            self.genes.append(chr(random.randrange(32, 123)))

    def createFitness(self):
        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == self.target[i]:
                score = score + 1

        self.fitness = score / len(self.target)

    def mutate(self):
        for i in range(len(self.genes)):
            if random.randrange(0, 100) < self.mutationRate:
                self.genes[i] = chr(random.randrange(32, 123))

    def crossover(self, partner):

        tempChild = DNA()
        midpoint = random.randrange(0, len(self.genes))

        for i in range(len(self.genes)):
            if i > midpoint:
                tempChild.genes[i] = self.genes[i]
            else:
                tempChild.genes[i] = partner.genes[i]

        return tempChild

    def getPhrase(self):
        return self.genes;

    # def createPopulation(self):
    #
    #     # for i in range(len(self.population)):
    #     #     self.population[i].createFitness()
    #
    #     for k in range(len(population)):
    #         n = int(population[k].fitness * 100)
    #
    #         for j in range(n):
    #             matingPool.append(population[k])

    # def reproduction(self):
    #     for i in range(len(self.population)):
    #
    #         while True:
    #             a = random.randrange(0, len(self.matingPool))
    #             b = random.randrange(0, len(self.matingPool))
    #
    #             parentA = self.matingPool[a]
    #             parentB = self.matingPool[b]
    #
    #             if not (parentA == parentB):
    #                 break
    #         # parentA = self.matingPool[a]
    #         # parentB = self.matingPool[b]
    #
    #         child = parentA.crossover(parentB)
    #         child.mutate()
    #         self.population[i] = child
    #     return child


# target = list("to be or not to be")

for i in range(totalPopulation):
    population.append(DNA())

# ob.createPopulation()
while state:
    # ob = DNA()
    # ob.createPopulation()
    matingPool = []
    for i in range(len(population)):
        population[i].createFitness()

    for k in range(len(population)):
        n = int(population[k].fitness * 100)

        for j in range(n):
            matingPool.append(population[k])

    for i in range(len(population)):

        while True:
            a = random.randrange(0, len(matingPool))
            b = random.randrange(0, len(matingPool))

            parentA = matingPool[a]
            parentB = matingPool[b]

            if not (parentA == parentB):
                break
        # parentA = self.matingPool[a]
        # parentB = self.matingPool[b]

        child = parentA.crossover(parentB)
        child.mutate()
        population[i] = child

    for i in range(len(population)):
        phrase = population[i].getPhrase()
        print(phrase, "Generation: ", generation)
        if phrase == target:
            state = False
            break

    generation = generation + 1

    # gene = ob.reproduction()
    # print(gene.genes)
    # if gene.genes == target:
    #     break
    # # print(ob.genes)
