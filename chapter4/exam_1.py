# 階上計算(再帰版)

def kaijo(n): # 再帰手続き
    if n==0:
        return 1
    else:
        return n*kaijo(n-1)

def main():
    for n in range(0, 13):
        print("%2d! = %10d"%(n, kaijo(n)))

if __name__=="__main__":
    main()
