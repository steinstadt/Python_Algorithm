# ハノイの塔(再帰解)
import sys, time

# 円盤の移動結果を出力
def print_hanoi(a, b, c):
    text = ""
    space = "    "
    # aの追加
    text += space + "aの円盤\n"
    for i in a:
        mark = " * "*(i)
        text += space + mark + "\n"
    text += "\n\n---------------------------\n"

    # bの結果
    text += space + "bの円盤\n"
    for i in b:
        mark = " * "*(i)
        text += space + mark + "\n"
    text += "\n\n---------------------------\n"

    # cの結果
    text += space + "cの円盤\n"
    for i in c:
        mark = " * "*(i)
        text += space + mark + "\n"
    text += "\n\n---------------------------\n"

    #結果の出力
    print(text, end="")

    # 1秒間スリープ
    time.sleep(1.5)

# aからbへの円盤の移動
def move_hanoi(a, b):
    a_num = a.pop(0) # aから値を取り出し
    b.insert(0, a_num)

def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1, a, c, b)
        move_hanoi(a, b)
        print_hanoi(a, b, c) # 円盤移動の途中結果を出力
        hanoi(n-1, c, b, a)

def main():
    num = int(input("円盤の枚数  ? "))

    a = [] # 最初は全ての円盤がここにある
    b = []
    c = []

    for i in range(0,num):
        a.append(i+1)

    hanoi(num, a, b, c)

if __name__=="__main__":
    main()
