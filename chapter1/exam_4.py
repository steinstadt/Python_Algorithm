# ユークリッドの互除法

def euclid():
    input_list = input("input number:") # 128 72の並びでくる
    input_list = input_list.split()

    m = int(input_list[0])
    n = int(input_list[1])
    while True:
        k = m % n
        m = n
        n = k
        if k==0:
            break

    print("最大公約数 = %d"%(m))

euclid()
