static, cost, sell = map(int, input().split())

if cost >= sell :
    print(-1)
else :
    print(static // (sell - cost) + 1)