from DNA import DNA
from random import randint,choice
class Population:
    def __init__(self):
        self.size = 20
        self.population = []
        self.matingPool = []
        self.maxFitness = 0
        self.mutationRate = 0.01 # 10% Mutation Rate
        # Generate Population
        for i in range(self.size):
            self.population.append(DNA())

    def evaluate(self):
        mf= 0
        # Calculate fitness 

        for i in self.population:
            i.getFitness()

        for i in self.population:
            if i.fitness > mf:
                mf = i.fitness
        
        for i in range(0,len(self.population)):
            if self.population[i].fitness == mf:
                print ("Fitness -> " + str(mf) + str(self.population[i].dna))
        self.maxFitness = mf
    def select(self):
        # selection
        self.matingPool = []
        newPopulation = []
        # calculate sum of fitness
        _sum = 0
        for i in self.population:
            _sum = _sum + i.fitness
        
        probs = []
        for i in self.population:
            p1 = round(i.fitness / _sum,2)
            probs.append(p1)

        for i in range(0,len(self.population)):
           for j in self.population:
            r1 = randint(0,int(_sum))
            if r1 < probs[i]:
                self.matingPool.append(j)

        
        for i in range(0,len(self.population)):
            pA = choice(self.matingPool)
            pB = choice(self.matingPool)

            child = pA.crossover(pB)
            child.mutation(self.mutationRate)
            

            newPopulation.append(child)

        self.population = newPopulation
