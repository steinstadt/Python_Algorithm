# 直接選択法

def main():

    NUM = 6 # データ数

    a = [80, 41, 35, 90, 40, 20] # データ
    min = 0 # 最小値

    for i in range(0, NUM-1):
        min = a[i]
        s = i
        for j in range(i+1, NUM):
            if a[j]<min:
                min = a[j]
                s = j
        # スワップ処理
        t = a[i]
        a[i] = a[s]
        a[s] = t

    for i in range(0, NUM):
        print("%d "%(a[i]), end="")

if __name__ == "__main__":
    main()
