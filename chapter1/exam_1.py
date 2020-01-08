# 漸化式(nCrの計算)

def combi(n, r):
    p = 1 #nC0 value
    # Dynamic Programming (bottom up type)
    for i in range(1, r+1):
        p = p*(n-i+1)/i
    return p

for n in range(0, 10):
    for r in range(0, n+1):
        print("%dC%d=%d "%(n, r, combi(n, r)), end="")
    print("")
