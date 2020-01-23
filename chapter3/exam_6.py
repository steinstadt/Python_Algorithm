# マージ(併合)

def main():
    a = [2, 4, 5, 7, 8, 10, 15, 20, 30, 40]
    b = [6, 11, 25, 33, 35]
    c = []

    i = 0
    j = 0
    while i < len(a) and j < len(b) : # a[], b[]とも終わりでない間
        if a[i]<b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1

    while i<len(a): # a[]が終わりになるまで
        c.append(a[i])
        i = i + 1

    while j<len(b): # b[]が終わりになるまで
        c.append(b[j])
        j = j + 1

    # 出力
    for i in range(0, len(a)+len(b)):
        print("%d "%(c[i]), end="")

if __name__=="__main__":
    main()
