M = int(input())
N = int(input())

li = []
for i in range(M, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i%j==0:
            # print("나머지 = 0")
            # print(cnt)
            cnt += 1
    if cnt==2:
        li.append(i)

total = -1
for i in li:
    total += i


if len(li)>0:
    total += 1
print(total)

if len(li)>0:    
    print(min(li))
    
