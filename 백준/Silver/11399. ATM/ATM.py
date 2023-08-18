N = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)

answer = 0
tmp = 0

while len(li)!=0:
    tmp += li.pop()
    answer += tmp
    
print(answer)