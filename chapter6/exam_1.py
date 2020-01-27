# ２分探索木への配列表現

class TreeNode():

    # コンストラクタ
    def __init__(self, left, name, right):
        self.left = left
        self.name = name
        self.right = right

def main():
    a = [
        TreeNode(1, "Machida", 2),
        TreeNode(3, "Canday", 4),
        TreeNode(5, "Rolla", None),
        TreeNode(None, "Ann", None),
        TreeNode(6, "Emy", 7),
        TreeNode(None, "Nancy", None),
        TreeNode(None, "Eluza", None),
        TreeNode(None, "Lisa", None)
    ]

    key = input("Search name-->")

    p = 0 # 配列ポインタ
    while not p==None:
        if key==a[p].name: # keyが見つかれば、出力
            print("見つかりました")
            break
        elif key<a[p].name:
            p = a[p].left
        else:
            p = a[p].right

if __name__=="__main__":
    main()
