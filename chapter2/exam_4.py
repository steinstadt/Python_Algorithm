# ２分法
import sys

# 対象となる関数
def f(x):
    return x*x*x-x+1

def main():
    LIMIT = 50 # 打ち切り回数
    EPS = 1e-8 # 打ち切り誤差

    low = -2.0 # 右端
    high = 2.0 # 左端
    x = 0

    for k in range(1, LIMIT+1):
        x = (low+high) / 2
        # 上限を半分に狭める処理
        if (f(x)>0):
            high = x
        else:
            low = x
        # 収束条件を満たしていれば,処理終了
        if(f(x)==0 or abs(high-low) < abs(low)*EPS):
            print("x=%f"%(x))
            return

    # 収束しない場合に,プリント終了
    print("収束しない")

if __name__ == '__main__':
    main()
