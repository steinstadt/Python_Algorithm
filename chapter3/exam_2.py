# バブルソート

def main():

    NUM = 6 # データ数
    a = [80, 41, 35, 90, 40, 20]

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
