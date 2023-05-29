from collections import Counter
import sys

input = sys.stdin.readline

def frequency_sort(data):
	rt_data = []
	for d, c in Counter(data).most_common():
		for i in range(c):
			rt_data.append(d)
	return rt_data

N, M = map(int, input().split())
li = []
li_cnt = []
for i in range(N):
    s = input()
    if len(s) >= M+1:
        li.append(s)

li.sort()                       # 사전순 정렬

li.sort(key=len, reverse=True)  # 길이순 정렬

li = frequency_sort(li)         # 빈도순 정렬

for i in list(dict.fromkeys(li)):
	print(i,end = '')