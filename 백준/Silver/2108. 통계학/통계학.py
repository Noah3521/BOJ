import math
import sys
from collections import Counter
input=sys.stdin.readline

Mean = 0
Median=0
Mode=0
rang=0
total=0
li = []
for _ in range(int(input())):
    tmp = int(input())
    li.append(tmp)
    total+=tmp
li.sort()

#산술평균값
Mean = round(total/len(li))
print(Mean)
#중앙값
Median = (li[len(li)//2])
print(Median)
#최빈값
f = Counter(li)

b = f.most_common() 

if len(li)==1:
    print(li[0])
if len(li)>1:
    if b[0][1]==b[1][1]:
        print(b[1][0])
    else :
        print(b[0][0])

#범위
print(li[-1] - li[0])