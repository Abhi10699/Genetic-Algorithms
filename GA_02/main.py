from Population import Population

if __name__ == '__main__':
    p = Population(1000,'My Name is abhi')
    while(not p.done):
        p.evaluate()
        p.select()
