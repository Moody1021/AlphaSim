
"""Agent module creates and manages agents in a multi dimensional universe in a cube
    shape. The edges wrap around. The first agent creation sets up the size of the
    universe and the number of dimenions.
"""

import utils
import random
import traceback
import sys

class Agent:
    """Manage agents in a universe of n dimensions n:2-20+."""
    alist = []  # all agents list
    nd = {}     # neighborhood dictionary of all agents when generated
    numagents = 0   # number of agents created. Also is the index of the agent into the agent list alist.
    size = 300  # size of universe
    
    def __init__(self, ndim, level):
        """Init agent with no coordinates in a cubic dimensional space of size ndim with level attribute"""
        self.level = level
        c = [None] * ndim
        self.coord = c
        self.dir = [None] * ndim
        # number of possible directions is 3**ndimensions,-1 since ix starts @ 0
        self.id = Agent.numagents
        self.neighborlist = []
        Agent.numagents += 1
        for i in range(ndim):
            self.dir[i] = random.randint(-1,1)
        Agent.alist.append(self)

    @classmethod
    def cdic(cls, nd, c, a):
        """Place an agent with a set of multi dimensional coordinates into a dictionary
           for later retrieval by coordinates or neighborhood.
        """
        if len(c) < 2:
            if c[0] in nd :
                nd[c[0]].append(a)
            else:
                nd[c[0]] = [ a ]
        else :
            if c[0] in nd:
                cls.cdic(nd[c[0]], c[1:], a)
            else :
                td = {}
                nd[c[0]] = td
                cls.cdic(td, c[1:], a)
        return

    @classmethod
    def nbrhood(cls):
        """Map all agents into a dictionary of neighbors for easy and quick retrieval
           for neighbor lists. The mapping is done by coordinates. Coordinates are used
           for retrieval of neighbors and neighborhoods. For each coordinate the dictionary
           holds a list of agents at that coordinate. Coordinate traversal is x,y,z,..
        """
        cls.nd = {}
        for i in cls.alist:
            cls.cdic(cls.nd, i.coord, i)

    def lvl(self, l=None):
        """Set or return an agents level"""
        if l != None:
            self.level = l
        return self.level
    
    def loc(self, coords=None):
        """Place agent at given coordinates. If no coordinates give, return agents coordinates.
        """
        j = 0
        if coords == None:
            return self.coord
        for i in coords:
            if i != None:
                self.coord[j] = i
                j += 1
        return self.coord

    @classmethod
    def cn(cls, d, c, depth, a):
        """Generate a list of neighbors at a given coordinate to a given depth, where depth
           is the distance from the coordinate to include in the neighbor list. Return the list of
           neighbors. d is dictionary, c coordinate, depth is how far from c to locate neighborhood.
           Don't insert self into list.
       """
        rl = []  
        if len(c) < 2:
            for i in range(-depth, depth+1):
                if ((c[0] + i)%cls.size) in d:
                    if a in d[(c[0]+i)%cls.size]:
                        tl = d[(c[0]+i)%cls.size][:]
                        tl.remove(a)
                        rl.extend(tl)
                    else:
                        rl.extend(d[(c[0]+i)%cls.size][:])
        else:
            for i in range(-depth, depth+1):
                if ((c[0]+i)%cls.size) in d:
                    rl.extend( cls.cn(d[(c[0]+i)%cls.size], c[1:], depth, a))
        if rl and abs(a.coord[0] - rl[0].coord[0]) > 2:
            print("We are off scale for neighbor")
        return rl                       

    def neighbors(self):
        """Generate a list of neighbors for an agent. neigbbors is an agent property."""
        self.neighborlist = []
        if not self.__class__.nd:
            self.nbrhood()
        self.neighborlist = self.__class__.cn(self.__class__.nd, self.coord, 1, self)

    def lvl(self, level=None):
        """Set or return an agents level."""
        if level != None:
            self.level = level
        return self.level
    
    @classmethod
    def place(cls, universe):
        """Place all agents randomly in the universe with no two agents at the same coordinates.
           Universe is given as the size of cube which holds all agents.        """
        n =  len(cls.alist)
        rl = utils.ranpop(n, universe)
        print("Number of Agents, universe size, # of agents", n, universe, len(rl))
        a = iter(cls.alist)
        for i in rl:
            next(a).loc(i)
            
    @classmethod
    def move(cls, size):
        """Move all agents by one step given the size of the universe. The edges of the universe wrap around.
        """
        dim = len(cls.alist[0].coord)
        for i in cls.alist:
            for j in range(dim):
                i.coord[j] = (i.dir[j] + i.coord[j]) % size

    @classmethod
    def reset(cls):
        """Clear the universe by destroying all agents."""
        cls.numagents = 0
        cls.alist = []

    @classmethod
    def list(cls):
        """List/print all agents, their level, and location."""
        for i in cls.alist:
            print( i.level, i.loc() )

    @classmethod
    def size(cls, size):
        """Set or return size of universe"""
        if size != None:
            cls.size = size
        return cls.size


