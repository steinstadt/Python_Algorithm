# 連立方程式（ガウス・ジョルダン法）

def main():
    N = 3

    # 係数行列
    coefficient_array = [
      [2.0, 3.0, 1.0, 4.0],
      [4.0, 1.0, -3.0, -2.0],
      [-1.0, 2.0, 2.0, 2.0]
    ]

    # 入力結果の表示
    print("連立方程式")
    for k in range(0,N):
        print("%dx + %dy + %dz = %d"% \
             (coefficient_array[k][0],\
              coefficient_array[k][1],\
              coefficient_array[k][2],\
              coefficient_array[k][3]))

    for pivot_key in range(0,N):
        p = coefficient_array[pivot_key][pivot_key] # ピボット係数

        # ピボット行をpで割る
        for j in range(pivot_key,N+1):
            coefficient_array[pivot_key][j] = coefficient_array[pivot_key][j] / p

        # ピボット列の掃き出し
        for i in range(0,N):
            if not i==pivot_key:
                d = coefficient_array[i][pivot_key] # ピボット行に掛ける係数
                for j in range(pivot_key,N+1):
                    coefficient_array[i][j] = coefficient_array[i][j] \
                                            - d \
                                            * coefficient_array[pivot_key][j]

    # 出力結果の表示（添え字いじってるの許してTT）
    print("")
    print("方程式の解")
    print("x = %f"%(coefficient_array[0][N]))
    print("y = %f"%(coefficient_array[1][N]))
    print("z = %f"%(coefficient_array[2][N]))

if __name__ == '__main__':
    main()
