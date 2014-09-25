import random
from functools import reduce

def ranpop(n, dim):
    size = reduce(lambda x, y: x*y, dim)
    if n > size:
        print("Population greater than sizez of the universe")
        return []
    rl = random.sample(range(size), n)
    ndim = len(dim)
    retlist = []
    #print("size, ndim, dim", size, ndim, dim)
    for j in rl:
        loc = j
        remains = j
        c = [None] * ndim
        i = ndim - 1
        while i > 0:
            tsize = reduce( lambda x, y: x*y, dim[:i])
            #print("i, loc, remains, tsize", i, loc, remains, tsize)
            c[i] = remains // tsize
            remains -= c[i] * tsize
            i -= 1
        c[0] = remains
        retlist.append(c)   
    return retlist   

if __name__ == '__main__':
    print("Running Unit test on module  utils\n")
    c = [10,20,100]
    c = [100,10,4]
    c = [6, 200, 10]
    num = 2501
    rl = ranpop(num, c)
    for i in rl:
        ix = 0
        for j in i:
            if c[ix] < j:
                print("Algorithm for dimensional placing ranpop not working: ix, c[ix], pos",ix,c[ix],j)
            ix += 1
            
                
