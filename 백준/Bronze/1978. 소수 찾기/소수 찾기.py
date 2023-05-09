N = int(input())

res = 0

li = list(map(int, input().split()))

for i in li:
    cnt = 0
    # print("i = ",i)
    for j in range(1, i+1):
        if i%j==0:
            # print("나머지 = 0")
            # print(cnt)
            cnt += 1
    if cnt==2:
        res += 1
print(res)