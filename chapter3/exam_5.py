# Pythonによるリストの探索

def main():

    a = [2, 3, 7, 11, 31, 50, 55, 70, 77, 80]

    key = int(input("探索するデータは？　："))

    # keyがリストに含まれているかどうか
    if key in a:
        index = a.index(key)
        print("%dは%d番目にありました"%(a[index], index+1))
    else: # keyがリストになければ、出力
        print("見つかりませんでした")

if __name__=="__main__":
    main()
