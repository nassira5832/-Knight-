
import random
class  Chromosome : 
    def __init__(self ,genes=None):
        self.genes = genes if genes else self._generate_random_genes()
    def _generate_random_genes(self):
        return [random.randint(0, 7) for _ in range(63)]
    def crossover(self, partner):
        crossover_point = random.randint(1, len(self.genes) - 1)
        p1 = self.genes[:crossover_point]
        p2 = partner.genes[crossover_point:]
        P = p1 + p2
        return Chromosome(P)
    def mutation (self, mutation_rate):
        for i in len(self.genes):
            if (random.random()<mutation_rate):
                self.genes[i] = random.randint(0, 7)
class  Knight :
    def __init__(self , position , chromosome , path , fitness=0):
        self.position=position
        self.position=position 
        self.chromosome = chromosome 
        self.path= path 
        self.fitness= fitness
    
        
    