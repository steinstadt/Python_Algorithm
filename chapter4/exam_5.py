# ハノイの塔（再帰解）
import os, time

class Hanoi():
    def __init__(self,n):
        self.num = n
        self.a = [] # 最初は全ての円盤がここにある
        self.b = []
        self.c = []

        # aを初期化
        for i in range(0,self.num):
            self.a.append(i+1)

    def exec(self,):
        self.hanoi(self.num, self.a, self.b, self.c)

    def hanoi(self, n, a, b, c):
        if n>0:
            self.hanoi(n-1, a, c, b)
            self.move_hanoi(a, b)
            self.print_hanoi() # 円盤移動の途中結果を出力
            self.hanoi(n-1, c, b, a)

    def move_hanoi(self, a, b):
        a_num = a.pop(0) # aから値を取り出し
        b.insert(0, a_num)

    def print_hanoi(self,):
        # タイトル出力
        print("==ハノイの塔==\n")

        # aの出力
        print("--aの円盤--")
        for i in self.a:
            mark = "* "*(i)
            print(mark)
        print("\n\n\n")

        # bの出力
        print("--bの円盤--")
        for i in self.b:
            mark = "* "*(i)
            print(mark)
        print("\n\n\n")


        # cの出力
        print("--cの円盤--")
        for i in self.c:
            mark = "* "*(i)
            print(mark)
        print("\n\n\n")

        # 1秒間スリープ
        time.sleep(1.5)

        # コンソール出力のクリア
        os.system('clear')

def main():
    num = int(input("円盤の枚数  ? "))
    hanoi_obj = Hanoi(num)
    hanoi_obj.exec()

if __name__=="__main__":
    main()
