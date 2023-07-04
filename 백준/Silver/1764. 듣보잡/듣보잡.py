import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = {}

count = 0
answer = []

for i in range(n):
    li[input()] = 1

for i in range(m):
    s = input()
    try :
        if li[s]==1:
            count += 1
            answer.append(s)
    except:
        pass

answer.sort()

print(count)
for i in answer:
    print(i, end ='')