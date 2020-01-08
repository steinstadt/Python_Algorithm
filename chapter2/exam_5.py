# ラグランジュ補間
import numpy as np
from matplotlib import pyplot as plt

x = [0.0, 1.0, 3.0, 6.0, 7.0] # 補間で使われるx座標
y = [0.8, 3.1, 4.5, 3.9, 2.8] # 補間で使われるy座標

output_x = [] # 補間で求められたx座標
output_y = [] # 補間で求められたy座標

# ラグランジュ補間を行う
def lagurange(x, y, n, t):
    s = 0.0
    for i in range(0,n):
        p = y[i]
        for j in range(0,n):
            if(i!=j):
                p = p*(t-x[j]) / (x[i]-x[j])
        s = s + p
    return s

def main():
    for t in np.arange(0.0, 7.5, 0.5):
        output_x.append(t)
        output_y.append(lagurange(x,y,5,t))

    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')

    plt.plot(x, y, marker='.', markersize=10, label='input') # 補間で使われる座標をプロット
    plt.plot(output_x, output_y, marker='.', markersize=10, label='output') # 補間結果をプロット
    plt.legend() # 凡例
    plt.show() # プロット結果を表示

if __name__ == '__main__':
    main()
