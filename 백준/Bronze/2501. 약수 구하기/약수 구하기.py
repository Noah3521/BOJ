N, K = map(int, input().split())
li = []
for i in range(1, N + 1) :
    if N%i==0:
        li.append(i)
li.sort()

if K > len(li):
    print(0)
else :
    print(li[K-1])