N = int(input())
length = list(map(int, input().split()))
cost = list(map(int, input().split()))

answer = 0

cursor = cost[0]

for i in range(len(cost)-1) :

    if cost[i] < cursor :
        cursor = cost[i] 
    answer += (length[i] * cursor)

print(answer)