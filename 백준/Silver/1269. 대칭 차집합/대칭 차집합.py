import sys
input = sys.stdin.readline
n,m=map(int, input().split())
a = {}
b = {}
s = list(map(int, input().split()))
for i in s:
    a[i] = 0
s = list(map(int, input().split()))
for i in s:
    b[i] = 0    


for i in a:
    try:
        if(b[i]==0):
            b[i] = 1
    except:
        pass
for i in b:
    try:
        if(a[i]==0):
            a[i] = 1
    except:
        pass

count = 0

for i in a:
    if(a[i]==0):
        count+=1
for i in b:
    if(b[i]==0):
        count+=1
print(count)