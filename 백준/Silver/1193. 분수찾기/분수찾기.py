N = int(input())
total = 0
for i in range(1,N+1):
    total+=i
    if N <= total:
        ib = total - i
        break
idx = i


if idx%2==0:
    for i in range(1, idx+1):
        if ib + i == N:
            print(f"{i}/{idx-i+1}")
else :
    for i in range(1, idx+1):
        if ib + i == N:
            print(f"{idx-i+1}/{i}")