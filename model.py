""" Setup the model universe
    create normal distribution of level of alpha 0-10. mean 5, sigma 2.
    create neighborhood of agents
    generate list of neighbors for each agent
    generate neighbor list for each agent
    add alpha rule
    
    
    
"""

import  pygame
import Agent
import queue
from time import sleep
import random

BOARDSIZE = 1024

class model:
    """Set up a model universe
    """
    univ = None # Universe space

    def __init__(self, qto, qfrom, size, numa, ndim):
        """Setup the model universe in size and dimensions
        """
        print("Model Start with size, agents, dimensions", size, numa, ndim)
        self.universeSize = size
        self.nDimensions = ndim
        self.numAgents = numa
        print("Usize, numa, ndim ", size, numa, ndim)
        pygame.init()
        model.univ = pygame.display.set_mode((size, size))
        Agent.Agent.size(size)
        al = []
        
        for i in range(0,  numa):
            al.append(Agent.Agent(ndim, int(random.normalvariate(5,2))))
        Agent.Agent.place([size, size])
        step = True
        generations = 0
        while True:
            generations += 1
            ev = pygame.event.poll()    # Look for any event
            if ev.type == pygame.QUIT:  # Window close button clicked?
                break    #   ... leave game loop
                        # Update your game objects and data structures here...
           
            # We draw everything from scratch on each frame.
            # So first fill everything with the background color
            #model.univ.fill((0,0,0))
            for i in al:
                model.univ.set_at(i.loc(), (255,0,0))

            # Now the surface is ready, tell pygame to display it!
            pygame.display.flip()

            if not qfrom.empty():
                msg = qfrom.get()
                if msg == "Start":
                    step = True
                if msg == "Stop":
                    break
                if msg == "Reset":
                    break
                if  msg == "Step":
                    step = False
                if msg == "Alpha":
                    print("Generations", generations)
                    nl = []
                    for i in al:
                        nl.append(len(i.neighborlist))
                    ns = sorted(set(nl), reverse=True)
                    print("Groups, size:",len(ns), ns)


            # clear the agents for their next move
            for i in al:
                model.univ.set_at(i.loc(), (0,0,0))
            Agent.Agent.move(size)
            #sleep(.1)
            Agent.Agent.nbrhood()
            for i in al:
                i.neighbors()
            self.alpharule(al)

        pygame.quit()     # Once we leave the loop, close the window.

    def alpharule(self, al):
        """find alpha in neigborlist and start following alpha by setting one's direction to alpha's direction/"""
        for i in al:
            for j in i.neighborlist:
                if j.level > i.level:
                    i.dir = j.dir

    def usize(self, size = None):
        """Set or return size of the universe"""
        if size != None:
            self.UniverseSize = size
        return self.universeSize

    def numdim(self, ndim=None):
        """Set or return number of dimensions in the universe"""
        if ndim != None:
            self.nDimensions = ndim
        return self.nDimensions

    def numagents(self, nag=None):
        """Set or return number of agents in the universe"""
        if nag != None:
            self.numAgents = nag
        return self.numAgents

    def show(self):
        if self.universeSize and self.nDimensions:
            surfaceSize = self.universeSize # Desired physical surface size, in pixels.

if __name__ == "__main__":
    """ Set up the game and run the main game loop """
    size = 300
    ag = 33
    dim = 2
    qf = queue.Queue()
    qt = queue.Queue()
    mod = model(qf, qt, 300, 33, 2)
    




