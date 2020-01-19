# バブルソート

import random

def main():

    NUM = 100 # データ数
    a = [] # データ

    # データの取得
    for i in range(0,NUM):
        a.append(1000*random.random())

    for i in range(0, NUM-1):
        for j in range(NUM-1, i, -1):
            if a[j]<a[j-1]:
                # スワップ処理
                t = a[j]
                a[j] = a[j-1]
                a[j-1] = t

    # 出力
    for i in range(0, NUM):
        print("%d "%(a[i]), end="")

if __name__ == "__main__":
    main()
