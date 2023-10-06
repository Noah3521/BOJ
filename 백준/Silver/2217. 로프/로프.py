import sys
input = sys.stdin.readline

li = []
n=int(input())
for i in range(n) : 
    li.append(int(input()))

li.sort()   

# print("최대값: ",max(li))

answer = li[-1]
temp = [li[-1]]
for i in range(n):
    if li[i]*(n-i) > li[-1] and max(temp) < li[i]*(n-i):
        answer = li[i]*(n-i)
        temp.append(li[i]*(n-i))

print(answer)