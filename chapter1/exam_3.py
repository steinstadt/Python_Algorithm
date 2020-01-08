# モンテカルロ法
import random

NUM = 1000

def calc_pi():
    count = 0
    for i in range(0,NUM):
        x = random.random()
        y = random.random()
        # 点が円内に入っているかを確認
        if (x*x+y*y<=1):
            count = count + 1

    pai = float(4*count/NUM)
    print("πの値=%f"%(pai))
    return

def calc_area():
    count = 0
    for i in range(0,NUM):
        x = 2*random.random()
        y = random.random()
        # 点が楕円内に入っているかを確認
        if (x*x/4+y*y<=1):
            count = count + 1

    s = 4.0*(2.0*count/NUM)
    print("楕円の面積 = %f"%(s))
    return

calc_area()
