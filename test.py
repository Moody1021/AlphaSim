
import Agent
import sys


def printdic(d):
    
    for key in d:
        if isinstance(d[key], list):
            for i in d[key]:
                print(" Key coord, Agentid", key, i.id)
        else:
            print("Key", key)
            printdic(d[key])

def printlist(l):
    for i in l:
        print(" id, coord", i.id, i.loc())

print("Testing neighbor list")

al = []
for i in range(40):
    al.append(Agent.Agent(2, 4))

Agent.Agent.place([20,20])
al[0].loc([10,15])
al[1].loc([9,17])

Agent.Agent.nbrhood()

for i in al:
    i.neighbors()
    print("Agent, id", i.id, i.loc())
    if i.neighborlist:
        printlist(i.neighborlist)
    


sys.exit()
print("Testing dictionary")
for i in al:
    print("Agent, id", i.id, i.loc())
printdic(Agent.Agent.nd)

sys.exit()
    

print("Testing neighborhood")

d = {}

ca = [1, 2, 5, 6]
Agent.Agent.cdic(d,ca,22)

cb = [1,2,5, 7]
Agent.Agent.cdic(d,cb,25)

cd = [2,2,5, 7]
Agent.Agent.cdic(d,cd,26)
ce = [3,2,5, 7]
Agent.Agent.cdic(d,ce,27)

print(d)
  
sys.exit()

a = Agent.Agent(3, 4)
print(a.lvl())
sys.exit()

class x:
    a = 5
    def b(self):
        print(self.a)

c = x()
c.b()
sys.exit()

 

a = Agent.Agent(3)
b = Agent.Agent(3)
c = Agent.Agent(3)
d = Agent.Agent(3)

Agent.placeall(20,20)



