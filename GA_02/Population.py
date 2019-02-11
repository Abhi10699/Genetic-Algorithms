from DNA import DNA
from random import randint,choice,uniform
class Population:
    def __init__(self,size,target):
        self.size = size
        self.population = []
        self.mutation_rate = 0.01
        self.target = target
        
        # Initialise population
        for i in range(0,self.size):
            self.population.append(DNA(len(target)))

        self.maxFitness = 0
        self.matingPool = []
        self.done = False

    def evaluate(self):
        mf = 0 # max fitness
        mString = ''
        for i in self.population:
            i.calcFitness(self.target)

        for i in self.population:
            if i.fitness > mf:
                mf = i.fitness

        for i in self.population:
            if i.fitness == mf:
                print(self.toString(i.genes))
                if i.genes == list(self.target):
                    self.done = True

    def select(self):
        self.matingPool = []
        newPopulation = []
        
        # Calculate Sum of all fitness values
        _sum = 0
        for i in range(0,len(self.population)):
           _sum = _sum + self.population[i].fitness
        
        probablity = []
        for i in self.population:
            probablity.append(i.fitness / _sum)


        for i in range(0,len(probablity)):
            n = probablity[i] * 1000
            for j in range(0,int(n)):
                self.matingPool.append(self.population[i])

        for i in range(0,len(self.population)):
            pA = choice(self.matingPool)
            pB = choice(self.matingPool)
            child = pA.crossover(pB)
            child.mutation(self.mutation_rate)

            newPopulation.append(child)

        self.population = newPopulation

    def toString(self,l):
        newStr = ''
        for i in l:
            newStr = newStr + i

        return newStr
