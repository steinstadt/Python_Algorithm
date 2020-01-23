# フィボナッチ数列(再帰版)

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    for i in range(1, 21):
        print("%3d: %d"%(i, fib(i)))

if __name__=="__main__":
    main()
