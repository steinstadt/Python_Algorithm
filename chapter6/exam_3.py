# 式の木を用いた式の計算
class TreeNode():
    def __init__(self, left, ope, right):
        self.left = left
        self.right = right
        self.ope = ope

# 木の作成
def gentree(p, w):
    n = len(w)
    s = w[:n-1]

    # ノードの決定
    if ord('0')<=ord(w[n-1]) and ord(w[n-1])<=ord('9'):
        p.ope = int(w[n-1])
    else:
        p.ope = w[n-1]

    if not (p.ope=='-' or p.ope=='+' or p.ope=='*' or p.ope=='/'): # 文字が定数であれば
        p.left = None
        p.right = None
    else:
        p.right = TreeNode(None, None, None) # 右の部分木を初期化
        p.left = TreeNode(None, None, None) # 左の部分木を初期化
        p.right, s = gentree(p.right, s)
        p.left, s = gentree(p.left, s)

    return p, s

# 式の木の計算
def postfix(p):
    if not p==None:
        postfix(p.left)
        postfix(p.right)
        if p.ope=='+':
            p.ope = p.left.ope + p.right.ope
        elif p.ope=='-':
            p.ope = p.left.ope - p.right.ope
        elif p.ope=='*':
            p.ope = p.left.ope * p.right.ope
        elif p.ope=='/':
            p.ope = p.left.ope / p.right.ope

def main():
    root = TreeNode(None, None, None)
    expression = "53*64+2/-" # 5*3-(6+4)/2を計算

    root, s = gentree(root, expression)
    postfix(root)

    print("value=%d"%(root.ope))

if __name__=="__main__":
    main()
