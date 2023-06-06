N, K = map(int, input().split())

li = []

for _ in range(N):
    li.append(int(input()))

count = 0
# while K>0:
for i in reversed(li):
    if K<=0:
        break
    if K>=i:
        while K >= i:
            count+=1
            # print(K)
            K -= i
            # print(K)
            # print()
print(count)