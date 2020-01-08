# 順位付け

Num = 10

a = [56, 25, 67, 88, 100, 61, 55, 67, 76, 56]
juni = [0]*Num

for i in range(Num):
    juni[i] = 1
    for j in range(Num):
        if a[j]>a[i]:
            juni[i] = juni[i] + 1

print(" 得点　順位")
for i in range(Num):
    print("%6d%6d"%(a[i], juni[i]))
