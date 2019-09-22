from AbstractSimulation import AbstractSimulation
import random

class Rule90(AbstractSimulation):
    def __init__(self, number_steps, density, length):
        super().__init__(number_steps)
        self.density = density
        self.length = length

    def initialize_sim(self):
        current_state=[0]*self.length
        num_1=int(self.density*self.length)
        list_1 = random.sample(range(self.length), num_1)
        for i in list_1:
            current_state[i]=1
        self.current_state=current_state
        self.next_state = [0]*self.length
        self.time=0

    def run_one_step(self):
        self.time += 1
        for i in range(self.length):
            if self.current_state[i-1]==self.current_state[(i+1)%self.length]:
                self.next_state[i]=0
            else:
                self.next_state[i]=1
        self.next_state,self.current_state=self.current_state,self.next_state


    def print_sim_state(self):
        print("At time {} the state is {}".format(str(self.time).zfill(2), ''.join('.' if x==0 else str(x) for x in self.current_state)))

simulator1=Rule90(50,0.5,50)
simulator1.run()