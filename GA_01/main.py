from Population import Population
p = Population()
while(p.maxFitness < 1):
    p.evaluate()
    p.select()
