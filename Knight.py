
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
    def __init__(self, chromosome=None):
        self.position = (0, 0) 
        self.chromosome = chromosome if chromosome else Chromosome()  
        self.path = [self.position]  
        self.fitness = 0  
    def move_forward (self ,direction):
        x, y = self.position
        if (direction==1):
             dx, dy=(-2, +1)
        if (direction==2):
             dx, dy=(-1, +2)
        if (direction==3):
             dx, dy=(+1, +2)
        if (direction==4):
             dx, dy=(+2, +1)
        if (direction==5):
             dx, dy=(+2, -1)
        if (direction==6):
             dx, dy=(+1, -2)
        if (direction==7):
             dx, dy=(-1, -2)
        if (direction==8):
             dx, dy=(-2, -1)
        new_position = (x + dx, y + dy)
        self.position = new_position
        self.path.append(new_position)
        return new_position
    
    def move_backward (self,direction):
         
         if (direction==1):
             dx, dy=(-2, +1)
         if (direction==2):
             dx, dy=(-1, +2)
         if (direction==3):
             dx, dy=(+1, +2)
         if (direction==4):
             dx, dy=(+2, +1)
         if (direction==5):
             dx, dy=(+2, -1)
         if (direction==6):
             dx, dy=(+1, -2)
         if (direction==7):
             dx, dy=(-1, -2)
         if (direction==8):
             dx, dy=(-2, -1)
         self.position = (self.position[0] - dx, self.position[1] - dy)
         self.path.pop()
    def check_moves ( ):
        



        
    