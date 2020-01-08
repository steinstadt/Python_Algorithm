# 一様乱数(線形合同法)

def irnd(rndnum):
    rndnum=(rndnum*109+1021) % 32768
    return rndnum

def rnd():
    rndnum = 13
    for j in range(0,100):
        rndnum = irnd(rndnum)
        print("%8d"%(rndnum), end="")
    print("")

rnd()
