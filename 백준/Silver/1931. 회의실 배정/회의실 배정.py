import sys
input = sys.stdin.readline

N = int(input())

li = []

for i in range(N) :
    a,b = map(int, input().split())
    li.append([a, b])

# N = 11
# li = [
#     [1,4],
#     [3,5],
#     [0,6],
#     [5,7],
#     [3,8],
#     [5,9],
#     [6,10],
#     [8,11],
#     [8,12],
#     [2,13],
#     [12,14],
# ]
answer = 0

li.sort()
right_sorted = sorted(li, key=lambda x: x[1])

min_value = 0
for i in right_sorted :
    if min_value <= i[0] :
        min_value = i[1]
        answer += 1

    

print(answer)
