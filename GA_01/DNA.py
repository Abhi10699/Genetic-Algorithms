from random import randint,random

class DNA:
    def __init__(self,dna=None):
        self.max = 50
        if(not dna == None):
            self.dna = dna
        else:
            self.dna = [randint(0,self.max),randint(0,self.max)]
            self.fitness = 0.0

    def getFitness(self):
        a = self.dna[0]
        b = self.dna[1]
        
        equation = abs(a + b - 87) # Find values of and A and B such that a + b = 15
        fitness = round(1 / (1+equation),3)

        if equation == 0:
            fitness = fitness + 0.1
        self.fitness = round( fitness ,3) 
    def crossover(self,partner):
        newGene = [self.dna[0],partner.dna[1]]
        return DNA(newGene)

    def mutation(self,mutationRate):   
        for i in range(0,len(self.dna)):
            if random() < mutationRate:
                self.dna[i] = randint(0,self.max)
