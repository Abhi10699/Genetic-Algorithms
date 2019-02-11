from random import randint,random,uniform,choice
class DNA:
    def __init__(self,s_len,genes=None):
        self.strlen = s_len
        if not genes == None:
            self.genes = genes
        else:
            self.genes = []
            for i in range(0,s_len):
                rC = chr(randint(31,125)) # Generate Random Characters
                self.genes.append(rC)


    def calcFitness(self,target):
        t = list(target)
        fitness = 0
        for i in range(0,len(self.genes)):
            if t[i] == self.genes[i]:
                fitness = fitness + 1
            else:
                fitness = fitness + 0.1
        self.fitness = fitness/len(target);

    
    def crossover(self,partner):
        newGene = []
        for i in range(0,len(self.genes)):
            if i  == 0:
                newGene.append(self.genes[i])
            else:
                newGene.append(partner.genes[i])
        
        return DNA(self.strlen,newGene)


    def mutation(self,mRate):
        for i in range(0,len(self.genes)):
            if uniform(0,1) < mRate:
                self.genes[i] = chr(randint(31,125))
            else:
                pass
