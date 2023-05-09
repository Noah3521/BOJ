import math
def ACM():
    H, W, N = map(int, input().split())
    #H:row W:col N:cnt
    # 호
    x = math.ceil(N/H)
    #층 
    y = N%H
    if y==0:
        y = H

    # print(f"{y}층")
    # print(f"{x}호")
    if x < 10:
        print(f"{y}"+"0"+f"{x}")
    else:
        print(f"{y}"+f"{x}")
T = int(input())
for i in range(T):
    ACM()