import sys 
input = sys.stdin.readline

N = int(input())

li = set()
count = 0

for i in range(N):
    s = input()
    if s=="ENTER\n":
        count+=len(li)
        li = set()
        continue
    li.add(s)

count += len(li)
print(count)   