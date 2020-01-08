# シンプソンの定積分
import math

# 被積分関数
def f(x):
    return math.sqrt(4-x*x)

start_end_nums = input("積分区間 : ")
a, b = map(int, list(start_end_nums.split())[0:2])

n = 50 # a~b間の分割数
h = (b-a) / (2*n) # 区間幅
fo = 0 # 奇数項の合計
fe = 0 # 偶数項の合計

for k in range(1, 2*n-2, 2):
    fo = fo + f(a+h*k)
    fe = fe + f(a+h*(k+1))

#面積の合計
sum = (f(a)+f(b)+4*(fo+f(b-h))+2*fe) * h/3

print("シンプソン則による定積分結果は" + str(sum) + "です。")
