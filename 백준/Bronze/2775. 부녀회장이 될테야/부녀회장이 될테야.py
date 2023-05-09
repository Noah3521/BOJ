def citizen():
    k = int(input()) # 층
    n = int(input()) # 호

    li = [i for i in range(1, n+1)]
    # print(li)
    res = 1
    for i in range(1, k+1):
        for j in range(1, n):
            li[j] += li[j-1]
            res = li[j]
    print(res)

for i in range(int(input())):
    citizen()