# 最小二乗法
import numpy as np
from matplotlib import pyplot as plt

def main():

    NUM = 7 # データ数
    DIM = 5 # 当てはめ次数

    # 取得データ
    x = [-3, -2, -1, 0, 1, 2, 3]
    y = [5, -2, -3, -1, 1, 4, 5]

    # 係数行列の準備(リスト内包表記)
    s = [0 for i in range(0,2*DIM+1)]
    t = [0 for i in range(0,DIM+1)]
    a = [[0]*(DIM+2) for i in range(DIM+1)] # 係数行列を格納する変数(DIM+1)*(DIM+2)

    for i in range(0, NUM):
        for j in range(0, 2*DIM+1): # s0からs2mの計算
            s[j] = s[j] + pow(x[i],j)
        for j in range(0, DIM+1): # t0からtmの計算
            t[j] = t[j] + pow(x[i],j)*y[i]

    # a[][]にs[],t[]の値を入れる
    for i in range(0, DIM+1):
        for j in range(0, DIM+1):
            a[i][j] = s[i+j]
        a[i][DIM+1] = t[i]

    # 掃き出し計算
    for k in range(0,DIM+1):
        p = a[k][k]
        for j in range(k,DIM+2): # ピボット行をpで割る
            a[k][j] = a[k][j] / p
        for i in range(0,DIM+1): # ピボット列の掃き出し
            if not i==k:
                d = a[i][k]
                for j in range(k,DIM+2):
                    a[i][j] = a[i][j] - d * a[k][j]

    # 近似式の出力
    print("関数の各係数")
    for k in range(0,DIM+1):
        print("a%d = %f"%(k, a[k][DIM+1]))

    # 近似式によるyの値の計算
    plot_x =  np.arange(-3, 3, 0.1)# プロット用のデータ
    plot_y = []
    for px in plot_x: # plot_xに対応するyを求める
        p = 0
        for k in range(0,DIM+1):
            p = p + a[k][DIM+1] * pow(px,k)
        plot_y.append(p)

    # プロット処理開始
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.plot(x, y, "bo",label='input', color='red')
    plt.plot(plot_x, plot_y, markersize=10, label='output') #近似式によるデータ補間
    plt.legend() # 凡例
    plt.show() # プロット結果を表示

if __name__ == "__main__":
    main()
