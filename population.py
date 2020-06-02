from DNA import *

class Population:
    def __init__(self):
        self.population = []

        for i in range(100):
            self.population.append(DNA())

    def crossover(self, patner):

        child = DNA()
        midpoint = random.randrange(0, len(self.genes) + 1)

        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = patner.genes[i]

        return child
