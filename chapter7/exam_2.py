# グラフの探索（幅優先探索）

N = 8 # 点の数

# 隣接行列
a = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0],
    [0,1,0,1,1,1,0,0,0],
    [0,0,1,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,1,1],
    [0,0,0,1,0,0,1,0,1],
    [0,0,0,0,0,0,1,1,0]
]

v = [0 for i in range(N+1)] # 訪問フラグ
queue = [0 for i in range(100)] # キュー

def main():

    for p in range(1,N+1):
        print("ノード%dを始点とする： "%(p),end="")
        for i in range(1,N+1): # フラグのクリア
            v[i] = 0
        head = 0
        tail = 0

        queue[tail] = p
        tail = tail + 1
        v[p] = 1

        while True: # 幅優先探索
            i = queue[head]
            head = head + 1
            for j in range(1,N+1):
                if a[i][j]==1 and v[j]==0:
                    print("%d->%d   "%(i,j), end="")
                    queue[tail] = j
                    tail = tail + 1
                    v[j] = 1

            if head==tail:
                break
        print("")

if __name__=="__main__":
    main()
