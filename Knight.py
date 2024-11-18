
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
 

    def check_moves(self):
   
      for i in range(len(self.chromosome.genes)):
          direction = self.chromosome.genes[i]
          self.move_forward(direction)

          if self.position[0] < 0 or self.position[0] >= 8 or self.position[1] < 0 or self.position[1] >= 8 or self.position in self.path:
             self.move_backward(direction)
             if random.choice([True, False]): 
                 cycle = self.get_forward_cycle(direction)
             else: 
                cycle = self.get_backward_cycle(direction)

             for t in cycle:
                self.move_forward(t)
                if self.position[0] >= 0 and self.position[0] < 8 and self.position[1] >= 0 and self.position[1] < 8 and self.position not in self.path:
                    self.chromosome.genes[i] = t
                    break
                else:
                    self.move_backward(t)
                    
             if self.position[0] < 0 or self.position[0] >= 8 or self.position[1] < 0 or self.position[1] >= 8 or self.position in self.path:
                self.chromosome.genes[i] = direction  

    def get_forward_cycle(self, direction):
      if direction == 1:
          return [2, 3, 4, 5, 6, 7, 8]
      elif direction == 2:
          return [3, 4, 5, 6, 7, 8, 1]
      elif direction == 3:
          return [4, 5, 6, 7, 8, 1, 2]
      elif direction == 4:
          return [5, 6, 7, 8, 1, 2, 3]
      elif direction == 5:
          return [6, 7, 8, 1, 2, 3, 4]
      elif direction == 6:
          return [7, 8, 1, 2, 3, 4, 5]
      elif direction == 7:
        return [8, 1, 2, 3, 4, 5, 6]
      elif direction == 8:
        return [1, 2, 3, 4, 5, 6, 7]

    def get_backward_cycle(self, direction):
      if direction == 1:
          return [8, 7, 6, 5, 4, 3, 2]
      elif direction == 2:
          return [1, 8, 7, 6, 5, 4, 3]
      elif direction == 3:
          return [2, 1, 8, 7, 6, 5, 4]
      elif direction == 4:
          return [3, 2, 1, 8, 7, 6, 5]
      elif direction == 5:
          return [4, 3, 2, 1, 8, 7, 6]
      elif direction == 6:
          return [5, 4, 3, 2, 1, 8, 7]
      elif direction == 7:
          return [6, 5, 4, 3, 2, 1, 8]
      elif direction == 8:
          return [7, 6, 5, 4, 3, 2, 1]
      
    def evaluate_fitness(self):
     fitness = 0
     visited_positions = set()
     for position in self.path:
        if not (0 <= position[0] < 8 and 0 <= position[1] < 8) or position in visited_positions:
            break
        visited_positions.add(position)
        fitness += 1
     if fitness == 64:
        return 64
     return fitness


class Population: 
    def __init__(self , population_size):
        self.population_size=population_size
        self.generation=1
        self. knights=[]
        for i in range(self.population_size):
            knight = Knight()  
            self.knights.append(knight)  
    def check_population(self):
        for i in self.knights : 
            i.check_moves()
    def evaluate(self):
        best_knight = None
        best_fitness = -1  
        for knight in self.knights:
            fitness = knight.evaluate_fitness()  
            if fitness > best_fitness:
                best_fitness = fitness
                best_knight = knight
        return best_knight, best_fitness
            
        
        
