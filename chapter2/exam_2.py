# 台形則による定積分
import math

# 被積分関数
def f(x):
    return math.sqrt(4-x*x)

start_end_nums = input("積分区間 ： ")
a, b = map(int , list(start_end_nums.split())[0:2])

n = 50 # a~bの分割数
h = (b-a) / n # 区間幅
x = a
s = 0 # f(a+h)+f(a+2h)+f(a+3h)...+f(a+(n-1)h)の値を求めるためのもの

for k in range(1, n):
    x = x + h
    s = s + f(x)

sum = h * (f(a)+f(b)/2 + s) # 面積の合計
print("台形則による定積分結果は" + str(sum) + "です。")
