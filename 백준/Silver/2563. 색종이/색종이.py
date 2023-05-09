paper = [[0]*101 for i in range(101)]

N = int(input())

for x in range(N):
    a, b =  map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] += 1

count = 100*N
for i in range(1, 101):
    for j in range(1, 101):
        if paper[i][j] > 1:
            count -= paper[i][j] - 1

print(count)