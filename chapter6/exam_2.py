# 式の木

class TreeNode():
    def __init__(self, left, ope, right):
        self.left = left
        self.ope = ope
        self.right = right

def gentree(p, w):
    n = len(w)

    p.ope = w[n-1] # 文字の後ろを取り出す
    s = w[:n-1]
    if not (p.ope=='-' or p.ope=='+' or p.ope=='*' or p.ope=='/'): # 文字が定数であれば
        p.left = None
        p.right = None
    else:
        p.right = TreeNode(None, None, None) # 右の部分木を初期化
        p.left = TreeNode(None, None, None) # 左の部分木を初期化
        p.right, s = gentree(p.right, s)
        p.left, s = gentree(p.left, s)

    return p, s

def postfix(p):
    if not p==None:
        postfix(p.left)
        postfix(p.right)
        print(p.ope, end='')

def main():
    root = TreeNode(None,None,None)
    expression = "ab*cd+e/-"

    root, s = gentree(root, expression) # 木の作成

    # 結果の出力
    print("postfix = ", end="")
    postfix(root)

if __name__=="__main__":
    main()
