# 線形計画法

def main():
    ROW = 4 # 係数行列の行数
    COL = 6 # 列数
    NUM = 2 # 変数の数

    coefficient_array = [
        [10, 30, 1, 0, 0, 180],
        [20, 30, 0, 1, 0, 210],
        [30, 10, 0, 0, 1, 210],
        [-20, -10, 0, 0, 0, 0]
    ]

    x = 0 # 行の添え字
    y = 0 # 列の添え字
    pivot = 0 # ピボット係数

    while True:
        min = 9999
        # 列の選択
        for k in range(0,COL-1):
            if coefficient_array[ROW-1][k]<min:
                min = coefficient_array[ROW-1][k]
                y = k

        if min==0:
            break

        min = 9999
        # 行の選択
        for k in range(0, ROW-1):
            p = coefficient_array[k][COL-1] / coefficient_array[k][y]
            if coefficient_array[k][y] > 0 and p < min:
                min = p
                x = k

        pivot = coefficient_array[x][y]
        # ピボット行をpで割る
        for k in range(0, COL):
            coefficient_array[x][k] = coefficient_array[x][k] / pivot
        # ピボット列の掃き出し
        for k in range(0, ROW):
            if k!=x:
                d = coefficient_array[k][y]
                for j in range(0, COL):
                    coefficient_array[k][j] = coefficient_array[k][j] - d * coefficient_array[x][j]

    # 結果の表示
    for k in range(0,NUM):
        flag = -1
        for j in range(0, ROW):
            if coefficient_array[j][k]==1:
                flag = j
        if flag!=-1:
            print("x%d = %f"%(k, coefficient_array[flag][COL-1]))
        else:
            print("x%d = %f"%(k, 0))
    print("最大値 : z = %f"%(coefficient_array[ROW-1][COL-1]))

if __name__ == "__main__":
    main()
