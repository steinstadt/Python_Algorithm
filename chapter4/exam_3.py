# 順列生成

def perm(p, i, NUM):
    if i<NUM-1: # 脱出条件
        for j in range(i, NUM):
            # スワップ処理
            t = p[i]
            p[i] = p[j]
            p[j] = t

            # n-1個の順列
            perm(p, i+1, NUM)

            # 元に戻すスワップ処理
            t = p[i]
            p[i] = p[j]
            p[j] = t
    else:
        for j in range(0,4):
            print("%d "%(p[j]), end="")
        print("")

def main():

    NUM = 4 #　データ数
    p = [] #　データ列

    for i in range(1,5): # データ初期化
        p.append(i)

    perm(p, 0, NUM)

if __name__=="__main__":
    main()
