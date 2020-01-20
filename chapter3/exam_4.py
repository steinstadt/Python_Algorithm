# ２分探索法

def main():

    # データ数
    NUM = 10

    a = [2, 3, 7, 11, 31, 50, 55, 70, 77, 80]

    # 探索するキーの入力
    key = int(input("探索するデータは？　："))

    low = 0 # 探索する下限
    high = NUM-1 # 探索する上限
    flat = 0 # 見つかったかどうかを表す変数

    while low<=high:
        mid = int((low+high)/2)
        if a[mid]==key: # キーが見つかった場合
            print("%dは%d番目にありました"%(a[mid], mid+1))
            flag = 1
            break
        elif a[mid]<key:
            low = mid + 1
        else:
            high = mid - 1

    if not flag==1: # キーが見つからなかったら、出力
        print("見つかりませんでした")

if __name__ == "__main__":
    main()
